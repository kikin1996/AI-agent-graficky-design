# KURKO / Pohyb

Pro plakáty a billboardy se nepoužije. Pro budoucí digitální výstupy je následující návrh, nikoli ověřený animovaný manuál klienta.

- Krátká odezva ovládání: 150 ms.
- Jemný přechod nebo odhalení obsahu: 250 ms, ease-in-out. Hodnota navazuje na základní CSS webu.
- Marketingový přechod větší kompozice: přibližně 450 ms; není nutný u každého prvku.

Preferovat prolnutí a krátký posun bez odskakování, rotace a deformace loga. Logo může vstoupit jako celek; nekonstruovat novou animovanou podobu symbolu bez konkrétního zadání. Text musí být čitelný dostatečně dlouho.

Při prefers-reduced-motion vypnout pohyb a ponechat statický obsah. Pro videa připravit i statický klíčový snímek. Animace ani výkon na cílových zařízeních zatím nebyly testovány.
