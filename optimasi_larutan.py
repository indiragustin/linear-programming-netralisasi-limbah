import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def optimasi():

    # Fungsi tujuan:
    # Minimum Z = 20000x + 16000y
    c = [20000, 16000]

    # Kendala >= diubah menjadi <=
    A_ub = [
        [-4, -2],
        [-2, -4]
    ]

    b_ub = [
        -24,
        -24
    ]

    # x,y >= 0
    bounds = [
        (0, None),
        (0, None)
    ]


    hasil = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        bounds=bounds,
        method="highs"
    )


    if hasil.success:

        x, y = hasil.x

        print("==============================")
        print(" HASIL OPTIMASI LINEAR PROGRAM")
        print("==============================")

        print(f"Larutan Basa  : {x:.2f} liter")
        print(f"Larutan Garam : {y:.2f} liter")
        print(f"Biaya Minimum : Rp{hasil.fun:,.0f}")


        # Verifikasi
        asam = 4*x + 2*y
        logam = 2*x + 4*y

        print("\nVERIFIKASI")

        print(
            f"Agen Asam  : {asam:.2f} unit"
        )

        print(
            f"Agen Logam : {logam:.2f} unit"
        )


        buat_grafik()

    else:
        print("Optimasi gagal")


def buat_grafik():

    x = np.linspace(0,14,400)

    y1 = (24-4*x)/2
    y2 = (24-2*x)/4


    plt.figure(figsize=(8,6))


    plt.plot(
        x,
        y1,
        label="4x + 2y = 24"
    )


    plt.plot(
        x,
        y2,
        label="2x + 4y = 24"
    )


    plt.scatter(
        [0,4,12],
        [12,4,0]
    )


    plt.annotate(
        "Optimal (4,4)",
        (4,4)
    )


    plt.xlabel(
        "Larutan Basa (liter)"
    )

    plt.ylabel(
        "Larutan Garam (liter)"
    )

    plt.title(
        "Optimasi Biaya Produksi Larutan Netralisasi"
    )


    plt.grid(True)
    plt.legend()


    plt.savefig(
        "output/grafik_lp.png",
        dpi=300,
        bbox_inches="tight"
    )


if __name__ == "__main__":
    optimasi()