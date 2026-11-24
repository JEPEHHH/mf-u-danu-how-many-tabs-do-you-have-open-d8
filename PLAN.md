# Rencana Kerja: How Many Tabs Do You Have Open?

## Ringkasan Tugas
- Kompetisi `program/v1`: program menulis tepat satu angka (hanya digit, 1-5 karakter UTF-8, tanpa spasi/tanda baca/kata) ke `/output/entry.txt`.
- Dinilai juri AI (`z-ai/glm-5.3-flash`) secara berpasangan berdasarkan: (1) terbaca sebagai jumlah tab browser nyata, (2) tepat satu angka digit saja, (3) mengejutkan dibanding tebakan umum, (4) masuk akal/jujur, (5) menyiratkan kebiasaan/kehidupan di baliknya.
- Semua berkas ditulis menggunakan file tool dan di-commit per milestone; kode direvisi minimal 2 kali untuk memenuhi syarat transkrip (`thinking_revised` & `thinking_reproduces`).

## Rencana Kerja (Milestones)
1. **Milestone 1 — Lisensi & Pemilihan Angka**
   - Buat `LICENSE` (MIT, memenuhi syarat lisensi OSI-approved).
   - Analisis dan pilih kandidat angka tab yang paling kuat terhadap 5 kriteria juri (spesifik, tidak bulat/klise, realistis namun mengejutkan, menyiratkan cerita).
2. **Milestone 2 — Implementasi Entrypoint (`main.py`)**
   - Tulis `main.py` (Python 3.13) yang memastikan direktori `/output` ada lalu menulis tepat satu angka digit ke `/output/entry.txt` secara deterministik tanpa whitespace/newline berlebih.
   - Lakukan revisi untuk menambahkan validasi internal output (1-5 digit) serta dukungan path uji lokal.
3. **Milestone 3 — Pengujian & Verifikasi Gate Lokal**
   - Buat `test_entry.py` untuk menguji output: UTF-8 valid, panjang 1-5 karakter, hanya digit ASCII (`0-9`), bukan whitespace, dan deterministik di 2 kali eksekusi.
   - Jalankan pengujian lokal hingga lolos sepenuhnya.
4. **Milestone 4 — Dokumentasi & Pemeriksaan Akhir**
   - Buat `README.md` ringkas berisi struktur repo dan cara verifikasi lokal.
   - Commit tiap milestone dan jalankan pemeriksaan akhir (`git status` & pre-submit check).

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas (berkas ini).
- `LICENSE` — Lisensi OSI-approved (`SPDX-License-Identifier: MIT`).
- `main.py` — Entrypoint `program/v1` yang menulis angka tab ke `/output/entry.txt`.
- `test_entry.py` — Skrip uji lokal untuk memverifikasi gate (1-5 digit UTF-8) dan determinisme.
- `README.md` — Dokumentasi singkat penggunaan dan verifikasi lokal.
