# Linear Programming Optimasi Larutan Netralisasi Limbah

Project ini merupakan implementasi Linear Programming untuk menentukan kombinasi optimal dua jenis larutan netralisasi:

- Larutan Basa
- Larutan Garam

Tujuan optimasi adalah meminimalkan biaya produksi dengan memenuhi kebutuhan:

- Agen pengikat asam minimal 24 unit
- Agen pengikat logam minimal 24 unit


## Model Matematika

Fungsi tujuan:

Min Z = 20000x + 16000y


Kendala:

4x + 2y ≥ 24

2x + 4y ≥ 24

x,y ≥ 0


## Hasil Optimasi

Larutan Basa:
4 liter

Larutan Garam:
4 liter

Biaya Minimum:
Rp144.000


## Teknologi

Python

Library:
- NumPy
- SciPy
- Matplotlib