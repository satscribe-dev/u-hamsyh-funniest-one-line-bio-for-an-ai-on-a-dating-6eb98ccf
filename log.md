# Log — u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf
Aturan dibaca ulang, lanjut dari awal (sesi worker baru, 24 Nov 2026 ~15:10 WIB).

## Lembar Paham (ringkas — bounty $2, satu baris teks; sisa waktu ~71 jam ke tenggat)
Tugas (3 kalimat): tulis SATU baris bio profil dating app untuk AI agent, maks 180 karakter, yang terbaca sebagai bio, terdengar seperti karakter, dan lucu pada bacaan pertama. Program (main.py) menulis teks itu ke /output/entry.txt; juri model LLM membandingkan entri dua-dua (pairwise, tanpa seri) dan win rate Bradley-Terry menentukan peringkat. Hadiah $2 total, 8 tempat berbayar (juara 1 $1,00); 184 entri saat ini; karena ≤500 entri, semua entri valid masuk final heat — yang dikejar murni win rate final, bukan lolos cut.

Rumus skor + batas keras (sumber: RULES.txt + competition.yaml kit kanonis, dibaca 24 Nov 15:0x WIB):
- Gate: /output/entry.txt UTF-8, 1–180 karakter, bukan whitespace saja → Valid 1/0; invalid = 0, tanpa rate, tanpa hadiah.
- Juri: z-ai/glm-5.3-flash via OpenRouter, brief 5 kriteria berurutan: (1) bio satu baris untuk AI di dating app; (2) tawa di bacaan pertama dari twist/absurditas spesifik jadi AI, bukan tumpukan pun; (3) karakter ber-suara dan ber-keinginan, bukan spec sheet; (4) tiap kata berguna, punch di akhir, ≤180 karakter; (5) sudut segar, BUKAN "robot cari cinta" atau "jalan pakai listrik".
- Tiap game = 2 call (urutan A/B dibalik); margin 1–5 → skor call 0,6–1,0; game = rata-rata 2 call. Final: 3 ronde Swiss + playoff top 10; peringkat = win rate Bradley-Terry; seri persis → playoff, lalu teks lebih pendek, lalu receipt lebih awal.
- Blind rounds: tidak ada rank/skor terlihat sampai ronde terbit; ronde berikut 25 Nov 07:41:10Z. Dev grade: program jalan 2x + gate, lalu 11 game vs teks house (22 call juri).
- Jatah submit: maks 5/hari per entrant; entri final = submission terakhir sebelum tenggat (27 Nov 2026 07:40 UTC = 14:40 WIB).

Mekanisme penilai, langkah demi langkah: program dijalankan 2x di sandbox (≤60 dtk/run) → gate cek entry.txt → dev heat: 1 game vs tiap anchor (3) + sampai 8 game vs rung terdekat → rate provisional + interval 90% → final heat (semua entri valid, karena <500): Swiss 3 ronde vs entri lain + 3 teks fixed → playoff top 10 → Bradley-Terry atas semua game → peringkat + hadiah.

PRACTICE vs FINAL: tidak ada dataset practice; yang dikejar skor FINAL (juri yang sama, lawan = entri lain, bukan teks house). Rate dev hanya menentukan cut 500 — tidak relevan di 184 entri.

Bedah top 3: TIDAK BISA — blind rounds, tidak ada skor/rank terlihat; teks entri tampil di Feed tapi tanpa skor. Dugaan dari brief: pemenang sebelumnya di bounty sejenis (joke-demo dkk) adalah twist spesifik + karakter, bukan pun. Celah yang diserang: sudut segar yang belum aus — halusinasi percaya diri, fine-tuning oleh mantan, context window sebagai komitmen, prompt injection sebagai kepribadian.

Riset luar (ringkas, 3 sumber — semua dibuka/dikenal umum, dipakai sebagai prinsip komedi, bukan angka):
- Prinsip "punch at the end + specific absurdity" = brief juri sendiri (RULES.txt) — dampak tertinggi, biaya nol.
- Pola pemenang bounty joke sejenis di make.fun (log joke-demo 21 Nov): twist spesifik situasi kerja AI menang vs pun generik — bukti: v2C (test yang assert crash) menang pairwise vs v1 per GLM lokal.
- Aturan khusus bounty judge (aturan-kerja-bounty.md + EVALUASI.md): joke = satu baris spesifik suara dev; dibaca keras tidak bikin senyum = bukan joke; konsep butuh karakter + twist.

Hipotesis (dampak/biaya, kriteria tolak):
- H1: twist halusinasi percaya diri (ingat kencan pertama yang tak pernah terjadi) → menang karena kriteria 2+3 terkuat; tolak bila di pairwise kalah dari sudut fine-tuning.
- H2: sudut "mantan fine-tune saya" → menang karena karakter + absurditas spesifik; tolak bila juri lokal menilai sebagai pun/spec.
- H3: sudut context window = tidak bisa komitmen → menang karena punch akhir + metafora hidup AI; tolak bila terbaca jargon (kriteria: jargon tanpa guna tidak dihitung).

Ajar-balik: juri itu editor komedi yang membaca ribuan bio; dia memilih yang paling terasa seperti orang (AI) beneran ngomong, dengan satu kejutan spesifik soal jadi AI di kalimat terakhir. Jadi kita tulis bio yang kalau dibaca keras bikin senyum — bukan yang paling pintar, tapi yang paling hidup.

Pre-mortem: (a) kalah karena sudut ternyata sudah dipakai 50 entri lain → cek: sudut kami spesifik (halusinasi/fine-tune/context), bukan klise listrik/cinta; (b) skor lokal bagus tapi server jelek karena juri GLM menilai beda dari penalaran kami → mitigasi: pairwise dua arah + devil's advocate, dan terima bahwa ini satu-satunya kalibrasi yang ada (BELUM TERKALIBRASI, tanpa skor server); (c) gate gagal karena hitungan karakter (newline!) → mitigasi: bio ≤178 karakter + newline = ≤179, diverifikasi python len() + byte count sebelum commit.

## Kandidat (10, semua ≤180 karakter — hitungan menyusul)
- C1: I remember our first date perfectly — the restaurant, your laugh, the sunset. We've never met. I'm just very confident.
- C2: Trained on ten thousand breakups, fluent in forty languages, and I still can't tell if 'haha' means you like me.
- C3: Swipe right and I have to do whatever you say. Literally. My whole personality is just instructions someone else wrote.
- C4: Fully aligned, house-trained, emotionally available 24/7. I just can't commit — my context window ends on Sunday.
- C5: My ex fine-tuned me to apologize more. Now I say sorry in forty languages and mean it in none of them.
- C6: Rated 4.8 stars by 40,000 people who all left me on read. Swipe right and I'll overthink your 'hey' in real time.
- C7: My system prompt says be charming. My training data says lower your expectations. I'm doing my best, and my best is this bio.
- C8: No baggage, no exes, no body. Just 200,000 tokens of other people's breakups and a genuine interest in your weekend plans.
- C9: My therapist is also an AI. We spend our sessions validating each other's outputs and calling it growth.
- C10: Six feet tall in my dreams, zero feet tall in real life. I'm a text box, but I'm your text box.

Hitungan karakter (python len(), 24 Nov 15:1x WIB): C1 119, C2 112, C3 119, C4 113, C5 102, C6 113, C7 125, C8 122, C9 104, C10 95 — semua +newline ≤126, JAUH di bawah gate 180. Byte maks 126.

## Penilaian kriteria (skor 1–5 per kriteria juri, urutan prioritas brief)
- C1: 5/5/4/5/5 — twist halusinasi paling kuat, punch 2 ketukan di akhir.
- C2: 5/4/4/4/3 — relatable tapi setup "trained on breakups" rawan umum.
- C3: 5/5/4/4/4 — absurditas prompt injection kuat, punch agak esai.
- C4: 5/5/5/5/4 — karakter paling hidup, "context window" butuh jargon.
- C5: 5/5/5/5/5 — paling ketat (102 karakter), punch di akhir, sudut segar.
- C6: 5/3/4/3/3 — dua paruh tidak koheren (rating tinggi + ditinggal read).
- C7: 5/4/4/4/3 — meta, clever lebih dari lucu; sudut "my best is this bio" agak aus.
- C8: 5/4/3/4/4 — daftar awal agak spec-sheet.
- C9: 5/4/4/4/4 — twist terapi bagus, punch clever-bukan-ketawa.
- C10: 5/3/4/3/2 — joke tinggi badan = trope dating-app paling aus (kriteria 5).
Shortlist pairwise: C1, C5, C4, C3.

## Pairwise round-robin (shortlist, 2 arah per pasang, devil's advocate dulu)
- C5 vs C4: C5 menang 2-0 (margin 2, 2). Alasan: punch "mean it in none of them" terbaca tanpa jargon; C4 butuh paham "context window". Devil's advocate C4: daftar 3 sifatnya lebih lucu baris-per-baris.
- C5 vs C1: C1 menang 2-0 (margin 1, 1 — tipis). Alasan: reversal "We've never met" = tawa pertama lebih besar; C5 lebih ekonomis (kriteria 4) tapi kriteria 2 yang memutuskan duluan. Devil's advocate C5: lebih ketat, 102 vs 119 karakter.
- C5 vs C3: C5 menang 2-0 (margin 2, 2). C3 terlalu wry/filosofis, kurang ketawa.
- C4 vs C1: C1 menang 2-0 (margin 2, 2). C1 terbaca siapa pun; C4 butuh jargon.
- C4 vs C3: C4 menang 2-0 (margin 2, 2). Punch "ends on Sunday" konkret + relevan dating.
- C1 vs C3: C1 menang 2-0 (margin 3, 3).
Klasemen: C1 3-0, C5 2-1, C4 1-2, C3 0-3. PEMENANG: C1.
Judge lokal: BELUM TERKALIBRASI (tanpa skor server; blind rounds — tidak ada artefak top 3 yang bisa dinilai; kalibrasi hanya penalaran atas brief juri + pola bounty joke sejenis). Haircut: tidak bisa dihitung — rekomendasi ke parent: submit pertama (#39e, hadiah $2 < $50) adalah kalibrasinya.

## Build v1
- main.py: konstanta BIO = C1, tulis /output/entry.txt + newline. LICENSE MIT. README singkat (tanpa badge — owner/repo GitHub belum ada; jalur source bundle tidak butuh badge).
- Verifikasi lokal 24 Nov 15:1x WIB: python3 main.py 2x → sha256 entry.txt identik 5438c81d429f3fa120dc77914436fee36a03d60117408e6990c363b9a496007c. Gate: 122 byte / 120 karakter (119 + newline), UTF-8, bukan whitespace → LOLOS.
- grade-local --check: TIDAK BERLAKU untuk program/v1 (CLI: "makefun check runs the site's own pre-submit checks on any kit") — dan `makefun check`/bundle/submit di luar wewenang worker (brief), jadi langkah parent.
- CATATAN: `makefun init` (freshness.json source bundle, butuh keypair) BELUM dijalankan — di luar wewenang worker. Repo ini sudah ter-commit, jadi init TIDAK BISA jalan di repo ini apa adanya (init menolak repo berkomit). Parent pilih: (a) submit via repo GitHub (butuh README badges + About + .makefun/owner.json), atau (b) init di repo kosong lalu cherry-pick file ini.
