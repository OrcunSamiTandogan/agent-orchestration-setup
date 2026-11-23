# Sık sorulan sorular

**İkisini de kurmam gerekiyor mu?** Hayır. Yalnız Pi, yalnız DSH veya ikisini seçebilirsin. Pi için NVIDIA, DSH için EVREN anahtarı kullanılır. Bunlar aynı anahtar değildir.

**EVREN’i kimler kullanabiliyor?** EVREN, Türkiye Cumhuriyeti vatandaşlarına açıktır ve e-Devlet doğrulaması kullanır. EVREN erişimin yoksa, NVIDIA erişimin varsa yalnız Pi ile başlayabilirsin.

**Claude Code veya Codex şart mı?** Hayır. Zaten kullanıyorsan kuruluma veya teyide yardımcı olabilirler. İstersen [manuel kurulum](manuel-kurulum.md) yolunu seçebilirsin.

**Anahtarı kurulum promptuna yazabilir miyim?** Hayır. Anahtarını sadece uygulamanın maskelenmiş yerel alanına gir. Anahtar dosyasını veya ayıklanmamış oturum kayıtlarını paylaşma.

**Kurulu araç neden uygulamada görünmüyor?** Sürümünü ve PATH ayarını uygulamadaki **Terminal** bölümünde kontrol et. Pi için Node.js 22.19+, DSH için 24.9+ gerekir. Yeniden kurmadan önce npm ve tmux durumuna da bak. Eksik bir araç varsa [ilk açılış rehberine](first-run.md) bak.

**DSH CLI ile DSH Web arasındaki fark nedir?** CLI, tmux içinde çalışan metin terminalidir. Web seçeneği DeepSeek Harness’ın tarayıcı arayüzünü açmayı ister. [DSH rehberi](evren-dsh.md)

**Sağlayıcı yavaşsa veya cevap vermiyorsa ne yapmalıyım?** Kurulumu değiştirmeden önce erişimini ve kotanı kontrol et. Pi’de `/model` ile başka bir NVIDIA modeli seçebilirsin. DSH bağlantısı DeepSeek V4.1 Flash kullanır ve sessizce başka modele geçmez.

**Dil seçimi ne zaman uygulanır?** Sol üstteki **Language / Dil** alanından dili seç ve uygulamayı hazır olduğunda yeniden aç. Tercihi değiştirmek açık oturumları kendi başına kapatmaz.

**macOS ve Windows test edildi mi?** Bu iki yol henüz önizleme. [Doğrulama notları](kalite.md)
