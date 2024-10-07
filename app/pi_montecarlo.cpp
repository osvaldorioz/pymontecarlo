#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <random>
#include <thread>
#include <vector>
#include <cmath>
#include <functional>

//c++ -Ofast -Wall -shared -std=c++20 -fPIC $(python3.12 -m pybind11 --includes) pi_montecarlo.cpp -o pi_montecarlo$(python3.12-config --extension-suffix)

namespace py = pybind11;

// Función para generar puntos aleatorios y contar cuántos caen dentro del círculo
void monte_carlo_pi(int num_points, int& points_in_circle) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    points_in_circle = 0;

    for (int i = 0; i < num_points; ++i) {
        double x = dis(gen);
        double y = dis(gen);
        if (x * x + y * y <= 1.0) {
            points_in_circle++;
        }
    }
}

// Función que divide el trabajo entre varios hilos
double concurrent_monte_carlo_pi(int total_points, int num_threads) {
    int points_per_thread = total_points / num_threads;
    std::vector<std::thread> threads;
    std::vector<int> results(num_threads, 0);

    // Lanzar hilos
    for (int i = 0; i < num_threads; ++i) {
        threads.emplace_back(monte_carlo_pi, points_per_thread, std::ref(results[i]));
    }

    // Esperar a que todos los hilos terminen
    for (auto& thread : threads) {
        thread.join();
    }

    // Sumar los resultados de todos los hilos
    int total_in_circle = 0;
    for (int result : results) {
        total_in_circle += result;
    }

    // Calcular la aproximación de Pi
    return 4.0 * static_cast<double>(total_in_circle) / static_cast<double>(total_points);
}

// Código para exponer las funciones a Python usando PyBind11
PYBIND11_MODULE(pi_montecarlo, m) {
    m.def("concurrent_monte_carlo_pi", &concurrent_monte_carlo_pi, "Calcular Pi usando Monte Carlo y concurrencia",
          py::arg("total_points"), py::arg("num_threads"));
}
