

| Параметр                 | Описание                            | Диапазон / Возможные значения                                                             |
| ------------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------- |
| `AnalogueGain`           | Аналоговое усиление (ISO)           | \~1.0–16.0 (1.0 ≈ ISO 100; 8.0 ≈ ISO 800)                                                 |
| `ExposureTime`           | Выдержка (в мкс)                    | \~100–1000000 (0.1 мс до 1 сек)                                                           |
| `Brightness`             | Яркость                             | -1.0 – +1.0 (обычно шаг 0.1)                                                              |
| `Contrast`               | Контраст                            | 0.0 – 32.0                                                                                |
| `Saturation`             | Насыщенность                        | 0.0 – 32.0                                                                                |
| `Sharpness`              | Резкость                            | 0.0 – 16.0                                                                                |
| `AeEnable`               | Автоэкспозиция                      | `True` / `False`                                                                          |
| `AwbEnable`              | Автоматический баланс белого        | `True` / `False`                                                                          |
| `AwbMode`                | Режим баланса белого                | `'auto'`, `'tungsten'`, `'fluorescent'`, `'indoor'`, `'daylight'`, `'cloudy'`, `'custom'` |
| `ColourGains`            | Баланс белого вручную               | `(R, B)` – например (1.0–8.0, 1.0–8.0)                                                    |
| `FrameDurationLimits`    | Ограничения FPS (в мкс)             | `(min_frame_time, max_frame_time)` – например `(10000, 33333)` для 30–100 FPS             |
| `NoiseReductionMode`     | Режим шумоподавления                | `'off'`, `'fast'`, `'high_quality'`                                                       |
| `AeMeteringMode`         | Тип экспозамера                     | `'centre-weighted'`, `'spot'`, `'matrix'`                                                 |
| `ExposureValue` (EV)     | Компенсация экспозиции              | float, примерно от -8.0 до +8.0                                                           |
| `ColourCorrectionMatrix` | Матрица цветокоррекции              | 3×3 матрица, задаётся вручную (для экспертов)                                             |
| `NoiseReductionStrength` | Сила шумоподавления (если включено) | 0.0 – 1.0                                                                                 |


```
#Example
picam2.set_controls({
    "AeEnable": False,             # Disable auto exposure
    "AwbEnable": False,            # Disable auto white balance
    "AnalogueGain": 2.0,           # ISO ≈ 200 (gain x100 gives approximate ISO)
    "ExposureTime": 10000,         # 10 ms exposure
    "ColourGains": (2.0, 1.5),     # Manual white balance (R gain, B gain)
})
```
