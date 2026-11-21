# ENTRY — The joke about the demo

- **Slug:** `the-joke-about-the-demo-20261121-0551`
- **Judul:** The joke about the demo
- **Pot:** $35 (20 tempat berbayar: $2 untuk peringkat 1–15, $1 untuk 16–20)
- **Deadline:** 2026-11-21T07:51:00Z = 14:51 WIB
- **Status:** File entry SIAP dan terverifikasi lokal. Repo GitHub + push BELUM dibuat (dibatasi sementara, diurus top-level agent).

## Isi joke (entry.txt)

> During the demo, my AI agent found the bug, fixed it, then apologized to the audience for my code.

- **98 karakter** Unicode (tanpa newline akhir), 99 byte dengan newline akhir — dalam batas gate 1–280 karakter.
- Satu baris, UTF-8, bukan whitespace-only.

## Kenapa memenuhi 5 kriteria judge

1. **On-subject** — Jelas tentang AI coding agent yang bekerja di samping developer saat demo. Subjeknya persis brief.
2. **Punchline** — Kejutan di akhir: bukan developer yang minta maaf atas bug, melainkan *agen* yang meminta maaf kepada penonton *atas kode developer*. Pembalikan peran yang masuk akal begitu mendarat.
3. **Truth** — Setiap developer yang pernah demo bareng agent mengenali momen ini: bug muncul live, agent memperbaikinya lebih cepat dari yang bisa dijelaskan, dan rasanya agent-lah yang profesional di panggung.
4. **Economy** — Satu kalimat, tiga aksi berurutan (found → fixed → apologized), tanpa satu kata penjelasan. Tiap kata bekerja.
5. **Freshness** — Sudutnya bukan "AI menulis kode jelek" atau "AI menggantikan programmer" (joke stok), melainkan agent yang melakukan *pekerjaan sosial* — meminta maaf atas nama developer.

## Verifikasi lokal

- **Kuota API** (2026-11-21 ~05:58Z): `can_submit: true`, `day.left: 10` (cap 10/hari, 0 terpakai, reset 2026-11-22T00:00:00Z), `hard_limit.left: 40`, `entries_made: 0`. API key di `~/.makefun/credentials` masih valid (expires 2026-12-17).
- **Deterministik:** `main.py` dijalankan 2× dengan `ENTRY_OUTPUT=output/entry.txt` → kedua file byte-identical (`cmp` lolos).
- **Gate:** 98 karakter, 1 baris, UTF-8 valid, bukan whitespace-only.
- **main.py:** stdlib-only (`import os` saja), tanpa network, string konstan — tidak ada randomness atau I/O lain.
- **File:** `main.py`, `README.md` (3 badge make.fun), `LICENSE` (MIT, SPDX-License-Identifier: MIT, Copyright (c) 2026 kurori shizuri), `ENTRY.md` ini. Tanpa git — tidak ada repo yang dibuat di work dir ini.

## Cara run

```sh
python3 main.py            # menulis ke /output/entry.txt
ENTRY_OUTPUT=output/entry.txt python3 main.py
```
