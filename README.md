# ChamaOS v2.1 🇰🇪
Sheng-aware, offline-first chama tracker built in Python on Android.

**Problem:** 80% of Kenyan chamas use notebooks. M-Pesa SMS get lost.
**Solution:** Type `nimelipa 1k 0712...` in Sheng, auto-parse amount + phone, store offline in SQLite, type `report` for instant totals.

**Stack:** Python, SQLite, Regex | Ready for WhatsApp Cloud API + Daraja M-Pesa API
**Built by:** Developer from Machakos, Kenya on Pydroid 3 (Android only)
**Live code:** chama.py

**Demo:**
nimelipa 1000 0712000012 -> Sawa! 0712000012 -> 1000 KES
report -> JUMLA YOTE: 1000 KES
