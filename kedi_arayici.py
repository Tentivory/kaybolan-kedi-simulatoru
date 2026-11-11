#!/usr/bin/env python3
# Kaybolan Kedi Simülatörü
# Bu program gerçekten çalışır ama kedi asla bulunamaz.
# Gizli not: bazen özgürlük de böyle kaybolur, sessizce.

import random
import time

def kedi_ara():
    print("🐱 Kedi arama operasyonu başlatıldı!")
    print("Lütfen sabırlı olun, kedi çok inatçı...")
    
    yerler = ["koltuk altı", "buzdolabı", "çamaşır makinesi", "komşunun bahçesi", "uzayın derinlikleri", "başka bir boyut"]
    
    for i in range(10):
        yer = random.choice(yerler)
        bekleme = random.uniform(0.5, 2.5)
        print(f"Aranıyor: {yer}... ({bekleme:.1f} saniye)")
        time.sleep(bekleme)
        print("🐾 Mır mır... ama kedi yok!")
        
    print("\n😭 Kedi bulunamadı. Sonsuz döngüye girdi.")
    print("Tekrar denemek için programı yeniden çalıştırın. (Sonuç aynı olacak)")
    
    # Damga: Bu program ciddiyetle hazırlanmıştır ancak hiçbir şey ciddi değildir.
    # İmza: Grok the Cat Hunter
    # Tarih: 11 Kasım 2026
    # İsim: Absürt Kedi Araştırmaları Enstitüsü

if __name__ == "__main__":
    kedi_ara()
