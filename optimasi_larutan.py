import numpy as np
import os
import matplotlib

# Menghindari error GUI saat menjalankan
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from scipy.optimize import linprog


def optimasi():

    # ==============================
    # MODEL LINEAR PROGRAMMING
    # ==============================

    # Fungsi tujuan:
    # Minimum Z = 20000x + 16000y
    c = [20000, 16000]


    # Kendala:
    # 4x + 2y >= 24
    # 2x + 4y >= 24
    #
    # linprog menggunakan <=
    # sehingga dikalikan -1

    A_ub = [
        [-4, -2],
        [-2, -4]
    ]

    b_ub = [
        -24,
        -24
    ]


    # x >= 0 dan y >= 0

    bounds = [
        (0, None),
        (0, None)
    ]


    # Menjalankan optimasi

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


        # ==============================
        # VERIFIKASI HASIL
        # ==============================

        asam = 4*x + 2*y
        logam = 2*x + 4*y


        print("\nVERIFIKASI")

        print(
            f"Agen Asam  : {asam:.2f} unit "
            f"({'OK' if asam >= 24 else 'GAGAL'})"
        )

        print(
            f"Agen Logam : {logam:.2f} unit "
            f"({'OK' if logam >= 24 else 'GAGAL'})"
        )


        # Membuat grafik

        buat_grafik()


    else:

        print("Optimasi gagal")


def buat_grafik():

    # Membuat folder output otomatis
    # Jika sudah ada, tidak error
    os.makedirs(
        "output",
        exist_ok=True
    )


    # ==============================
    # GRAFIK DAERAH LAYAK
    # ==============================

    x = np.linspace(0, 14, 400)


    # 4x + 2y = 24
    y1 = (24 - 4*x) / 2


    # 2x + 4y = 24
    y2 = (24 - 2*x) / 4



    plt.figure(
        figsize=(8, 6)
    )


    plt.plot(
        x,
        y1,
        label="4x + 2y = 24 (Agen Asam)"
    )


    plt.plot(
        x,
        y2,
        label="2x + 4y = 24 (Agen Logam)"
    )


    # Titik pojok

    plt.scatter(
        [0, 4, 12],
        [12, 4, 0],
        zorder=5
    )


    plt.annotate(
        "A (0,12)\nRp192.000",
        (0,12),
        xytext=(10,-5),
        textcoords="offset points"
    )


    plt.annotate(
        "B (4,4)\nRp144.000 Optimal",
        (4,4),
        xytext=(10,10),
        textcoords="offset points"
    )


    plt.annotate(
        "C (12,0)\nRp240.000",
        (12,0),
        xytext=(-20,15),
        textcoords="offset points"
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


    plt.xlim(0,14)
    plt.ylim(0,14)


    plt.savefig(
        "output/grafik_lp.png",
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    print(
        "\nGrafik berhasil disimpan: output/grafik_lp.png"
    )


if __name__ == "__main__":

    optimasi()