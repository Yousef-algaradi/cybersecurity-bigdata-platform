# 📈 النتائج والرؤى | Results & Insights

> **ملخص النتائج المستخلصة من EDA و Dashboard**

---

## 🎯 نظرة عامة

بعد معالجة **2,540,047 سجلاً** (ناتجة عن 2,540,044 سجلاً أصلياً في UNSW-NB15 + 3 سجلات إضافية من معالجة البيانات عبر NiFi/Kafka)، تم استخراج مجموعة من **الرؤى الأمنية** التي تكشف أنماط الهجمات السيبرانية وتوزيعها.

هذا الملف يعرض **أهم النتائج** المدعومة بالرسومات البيانية من ملفات EDA و Dashboard.

---

## 📊 1. توزيع Normal vs Attack

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الفئة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد السجلات</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النسبة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Normal</td><td style="padding: 8px; border: 1px solid #ddd;">2,218,764</td><td style="padding: 8px; border: 1px solid #ddd;">87.35%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Attack</td><td style="padding: 8px; border: 1px solid #ddd;">321,283</td><td style="padding: 8px; border: 1px solid #ddd;">12.65%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Total</b></td><td style="padding: 8px; border: 1px solid #ddd;"><b>2,540,047</b></td><td style="padding: 8px; border: 1px solid #ddd;"><b>100%</b></td></tr>
  </tbody>
</table>

### الرؤية

- **87% Normal** vs **13% Attack** → **Data Imbalance** واضح.
- التأثير: يحتاج ML Models معالجة خاصة (Class Weighting).

---

## 🛡️ 2. توزيع فئات الهجمات

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الفئة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد الهجمات</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النسبة من الهجمات</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Generic</td><td style="padding: 8px; border: 1px solid #ddd;">215,481</td><td style="padding: 8px; border: 1px solid #ddd;">67.07%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Exploits</td><td style="padding: 8px; border: 1px solid #ddd;">44,525</td><td style="padding: 8px; border: 1px solid #ddd;">13.86%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Fuzzers</td><td style="padding: 8px; border: 1px solid #ddd;">24,246</td><td style="padding: 8px; border: 1px solid #ddd;">7.55%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">DoS</td><td style="padding: 8px; border: 1px solid #ddd;">16,353</td><td style="padding: 8px; border: 1px solid #ddd;">5.09%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Reconnaissance</td><td style="padding: 8px; border: 1px solid #ddd;">13,987</td><td style="padding: 8px; border: 1px solid #ddd;">4.35%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Analysis</td><td style="padding: 8px; border: 1px solid #ddd;">2,677</td><td style="padding: 8px; border: 1px solid #ddd;">0.83%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Backdoors</td><td style="padding: 8px; border: 1px solid #ddd;">2,329</td><td style="padding: 8px; border: 1px solid #ddd;">0.72%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Shellcode</td><td style="padding: 8px; border: 1px solid #ddd;">1,511</td><td style="padding: 8px; border: 1px solid #ddd;">0.47%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Worms</td><td style="padding: 8px; border: 1px solid #ddd;">174</td><td style="padding: 8px; border: 1px solid #ddd;">0.05%</td></tr>
  </tbody>
</table>

### الرؤية

- **Generic** هي الأكثر (**67%** من الهجمات).
- **Worms** هي الأقل (**0.05%**).
- **Exploits** تأتي في المرتبة الثانية (**13.86%**).
- الفئات الخمس الأولى تمثل **98%** من الهجمات.

---

## 🌐 3. توزيع البروتوكولات

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">البروتوكول</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد السجلات</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النسبة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">TCP</td><td style="padding: 8px; border: 1px solid #ddd;">1,495,074</td><td style="padding: 8px; border: 1px solid #ddd;">58.86%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">UDP</td><td style="padding: 8px; border: 1px solid #ddd;">990,435</td><td style="padding: 8px; border: 1px solid #ddd;">39.00%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">UNAS</td><td style="padding: 8px; border: 1px solid #ddd;">16,202</td><td style="padding: 8px; border: 1px solid #ddd;">0.64%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ARP</td><td style="padding: 8px; border: 1px solid #ddd;">10,064</td><td style="padding: 8px; border: 1px solid #ddd;">0.40%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">OSPF</td><td style="padding: 8px; border: 1px solid #ddd;">7,798</td><td style="padding: 8px; border: 1px solid #ddd;">0.31%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SCTP</td><td style="padding: 8px; border: 1px solid #ddd;">1,525</td><td style="padding: 8px; border: 1px solid #ddd;">0.06%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ICMP</td><td style="padding: 8px; border: 1px solid #ddd;">524</td><td style="padding: 8px; border: 1px solid #ddd;">0.02%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">GRE</td><td style="padding: 8px; border: 1px solid #ddd;">324</td><td style="padding: 8px; border: 1px solid #ddd;">0.01%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">RSVP</td><td style="padding: 8px; border: 1px solid #ddd;">274</td><td style="padding: 8px; border: 1px solid #ddd;">0.01%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">أخرى</td><td style="padding: 8px; border: 1px solid #ddd;">~17,827</td><td style="padding: 8px; border: 1px solid #ddd;">~0.70%</td></tr>
  </tbody>
</table>

### الرؤية

- **TCP + UDP** = **98%** من الحركة.
- TCP أكثر من UDP بـ **1.5x**.

---

## 🎯 4. نسبة الهجمات في كل بروتوكول

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">البروتوكول</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Total Records</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Attack Count</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Attack %</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">TCP</td><td style="padding: 8px; border: 1px solid #ddd;">1,495,074</td><td style="padding: 8px; border: 1px solid #ddd;">58,184</td><td style="padding: 8px; border: 1px solid #ddd;">3.89%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">UDP</td><td style="padding: 8px; border: 1px solid #ddd;">990,435</td><td style="padding: 8px; border: 1px solid #ddd;">223,750</td><td style="padding: 8px; border: 1px solid #ddd;">22.59%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">UNAS</td><td style="padding: 8px; border: 1px solid #ddd;">16,202</td><td style="padding: 8px; border: 1px solid #ddd;">16,202</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ARP</td><td style="padding: 8px; border: 1px solid #ddd;">10,064</td><td style="padding: 8px; border: 1px solid #ddd;">0</td><td style="padding: 8px; border: 1px solid #ddd;">0%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">OSPF</td><td style="padding: 8px; border: 1px solid #ddd;">7,798</td><td style="padding: 8px; border: 1px solid #ddd;">3,278</td><td style="padding: 8px; border: 1px solid #ddd;">42.04%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SCTP</td><td style="padding: 8px; border: 1px solid #ddd;">1,525</td><td style="padding: 8px; border: 1px solid #ddd;">1,525</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ICMP</td><td style="padding: 8px; border: 1px solid #ddd;">524</td><td style="padding: 8px; border: 1px solid #ddd;">0</td><td style="padding: 8px; border: 1px solid #ddd;">0%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">GRE</td><td style="padding: 8px; border: 1px solid #ddd;">324</td><td style="padding: 8px; border: 1px solid #ddd;">324</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">RSVP</td><td style="padding: 8px; border: 1px solid #ddd;">274</td><td style="padding: 8px; border: 1px solid #ddd;">274</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
  </tbody>
</table>

### الرؤية

- **UNAS + SCTP + GRE + RSVP** = **100% هجمات** (لكن العينات صغيرة).
- **OSPF** = **42%** هجمات.
- **UDP** = **22.6%** هجمات (5.8x أكثر من TCP).
- **TCP** = **3.9%** هجمات.
- **ARP + ICMP** = **لم تُسجَّل هجمات** في البيانات المستخدمة.

**ملاحظة:** البروتوكولات ذات النسب 100% (UNAS, SCTP, GRE, RSVP) لها **عينات صغيرة جداً** (< 17K سجل)، لذا النسب قد لا تكون معبّرة إحصائياً.

---

## 🔍 5. نسبة الهجمات في كل خدمة

### النتائج (Top 10)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الخدمة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Total Records</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Attack %</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SSL</td><td style="padding: 8px; border: 1px solid #ddd;">142</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">DHCP</td><td style="padding: 8px; border: 1px solid #ddd;">172</td><td style="padding: 8px; border: 1px solid #ddd;">100%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">POP3</td><td style="padding: 8px; border: 1px solid #ddd;">1,533</td><td style="padding: 8px; border: 1px solid #ddd;">99.74%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">DNS</td><td style="padding: 8px; border: 1px solid #ddd;">781,668</td><td style="padding: 8px; border: 1px solid #ddd;">26.95%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">HTTP</td><td style="padding: 8px; border: 1px solid #ddd;">206,273</td><td style="padding: 8px; border: 1px solid #ddd;">9.14%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">None</td><td style="padding: 8px; border: 1px solid #ddd;">1,246,397</td><td style="padding: 8px; border: 1px solid #ddd;">6.41%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">FTP</td><td style="padding: 8px; border: 1px solid #ddd;">49,090</td><td style="padding: 8px; border: 1px solid #ddd;">6.14%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SMTP</td><td style="padding: 8px; border: 1px solid #ddd;">81,645</td><td style="padding: 8px; border: 1px solid #ddd;">6.11%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">FTP-Data</td><td style="padding: 8px; border: 1px solid #ddd;">125,783</td><td style="padding: 8px; border: 1px solid #ddd;">1.50%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SSH</td><td style="padding: 8px; border: 1px solid #ddd;">47,160</td><td style="padding: 8px; border: 1px solid #ddd;">0.04%</td></tr>
  </tbody>
</table>

### الرؤية

- **SSL + DHCP** = **100% هجمات** (لكن العينات صغيرة: < 200 سجل).
- **POP3** = **99.7%** هجمات (1,533 سجل).
- **DNS** = **27%** هجمات (نسبة عالية على عينة كبيرة).
- **SSH** = **0.04%** (أقل معدل هجمات ضمن الخدمات المعروضة).

**ملاحظة:** الخدمات ذات النسب 100% (SSL, DHCP) لها **عينات صغيرة جداً** (< 200 سجل)، لذا النسب قد لا تكون معبّرة إحصائياً.

---

## 🚦 6. توزيع حالات الاتصال

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الحالة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد السجلات</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النسبة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">FIN</td><td style="padding: 8px; border: 1px solid #ddd;">1,478,689</td><td style="padding: 8px; border: 1px solid #ddd;">58.22%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">CON</td><td style="padding: 8px; border: 1px solid #ddd;">560,588</td><td style="padding: 8px; border: 1px solid #ddd;">22.07%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">INT</td><td style="padding: 8px; border: 1px solid #ddd;">490,471</td><td style="padding: 8px; border: 1px solid #ddd;">19.31%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">REQ</td><td style="padding: 8px; border: 1px solid #ddd;">9,043</td><td style="padding: 8px; border: 1px solid #ddd;">0.36%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">RST</td><td style="padding: 8px; border: 1px solid #ddd;">528</td><td style="padding: 8px; border: 1px solid #ddd;">0.02%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">أخرى</td><td style="padding: 8px; border: 1px solid #ddd;">~728</td><td style="padding: 8px; border: 1px solid #ddd;">0.03%</td></tr>
  </tbody>
</table>

### الرؤية

- **FIN** = الأكثر (**58%**).
- **CON + INT** = **41%**.
- حالات أخرى قليلة جداً.

---

## 🌍 7. Top Source IPs

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Source IP</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد السجلات</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.4</td><td style="padding: 8px; border: 1px solid #ddd;">~197,959</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.1</td><td style="padding: 8px; border: 1px solid #ddd;">~197,680</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.5</td><td style="padding: 8px; border: 1px solid #ddd;">~197,626</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.2</td><td style="padding: 8px; border: 1px solid #ddd;">~197,550</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.0</td><td style="padding: 8px; border: 1px solid #ddd;">~197,527</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.3</td><td style="padding: 8px; border: 1px solid #ddd;">~195,953</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.9</td><td style="padding: 8px; border: 1px solid #ddd;">~190,187</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.6</td><td style="padding: 8px; border: 1px solid #ddd;">~189,419</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.8</td><td style="padding: 8px; border: 1px solid #ddd;">~189,341</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">59.166.0.7</td><td style="padding: 8px; border: 1px solid #ddd;">~189,059</td></tr>
  </tbody>
</table>

### الرؤية

- **توزيع متساوٍ** بين IPs (لا يوجد IP مشبوه بمفرده).
- كل الـ IPs من النطاق `59.166.0.x` (شبكة اختبار UNSW).

---

## 🌍 8. Top Destination IPs

### النتائج (Top 10)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Destination IP</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">عدد السجلات</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.3</td><td style="padding: 8px; border: 1px solid #ddd;">~197,771</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.2</td><td style="padding: 8px; border: 1px solid #ddd;">~197,648</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.4</td><td style="padding: 8px; border: 1px solid #ddd;">~197,639</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.1</td><td style="padding: 8px; border: 1px solid #ddd;">~197,535</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.5</td><td style="padding: 8px; border: 1px solid #ddd;">~197,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.0</td><td style="padding: 8px; border: 1px solid #ddd;">~196,770</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.9</td><td style="padding: 8px; border: 1px solid #ddd;">~190,483</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.7</td><td style="padding: 8px; border: 1px solid #ddd;">~190,268</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.6</td><td style="padding: 8px; border: 1px solid #ddd;">~189,709</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">149.171.126.8</td><td style="padding: 8px; border: 1px solid #ddd;">~187,479</td></tr>
  </tbody>
</table>

### الرؤية

- كل الـ IPs من النطاق `149.171.126.x` (شبكة اختبار UNSW).
- توزيع متساوٍ → **شبكة اختبار موحدة**.

---

## ⏰ 9. توزيع الهجمات حسب الساعة

### النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الساعة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Attack Count</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">0</td><td style="padding: 8px; border: 1px solid #ddd;">~1,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">~20,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">~15,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">~30,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">~28,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">~40,000 ← الذروة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">~20,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">~35,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">~20,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">~30,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">~20,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">11</td><td style="padding: 8px; border: 1px solid #ddd;">~30,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">12</td><td style="padding: 8px; border: 1px solid #ddd;">~20,000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">13</td><td style="padding: 8px; border: 1px solid #ddd;">~10,000</td></tr>
  </tbody>
</table>

### الرؤية

- **الذروة في الساعة 5** (~40K هجمة).
- **الساعات 3-5** = الأكثر نشاطاً.
- **الساعة 0** = الأقل.
- البيانات تغطي **13 ساعة فقط** (0-13).

---

## 📊 10. Time Series Analysis

### النتائج

- **الفترة:** 2015-01-21 إلى 2015-02-17.
- **عدد الأيام:** ~28 يوماً.
- **الاتجاه:** Normal مرتفع في البداية ثم استقر.
- **Attack:** توزيع ثابت نسبياً.

---

## 🎯 الرؤى الرئيسية (Top 10)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الرؤية</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الأهمية</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">87% Normal vs 13% Attack</td><td style="padding: 8px; border: 1px solid #ddd;">🔴 عالية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Generic = 67% من الهجمات</td><td style="padding: 8px; border: 1px solid #ddd;">🔴 عالية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">UNAS + SCTP + GRE + RSVP = 100% هجمات (عينة صغيرة)</td><td style="padding: 8px; border: 1px solid #ddd;">🟡 متوسطة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">SSL + DHCP = 100% هجمات (عينة صغيرة)</td><td style="padding: 8px; border: 1px solid #ddd;">🟡 متوسطة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">UDP = 22.6% هجمات (5.8x أعلى من TCP)</td><td style="padding: 8px; border: 1px solid #ddd;">🟡 متوسطة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">SSH = أقل معدل هجمات ضمن الخدمات المعروضة (0.04%)</td><td style="padding: 8px; border: 1px solid #ddd;">🟢 منخفضة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">الذروة في الساعة 5 (40K هجمة)</td><td style="padding: 8px; border: 1px solid #ddd;">🟡 متوسطة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">TCP = 58.86% من الحركة</td><td style="padding: 8px; border: 1px solid #ddd;">🟢 منخفضة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">توزيع متساوٍ بين IPs</td><td style="padding: 8px; border: 1px solid #ddd;">🟢 منخفضة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">ARP + ICMP: لم تُسجَّل هجمات في البيانات</td><td style="padding: 8px; border: 1px solid #ddd;">🟢 منخفضة</td></tr>
  </tbody>
</table>

---

## 🔗 الملفات المرتبطة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الملف</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الموضوع</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;"><b>00_overview.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">نظرة عامة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;"><b>01_architecture.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المعمارية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;"><b>02_dataset.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">البيانات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><b>03_pipeline.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><b>04_results.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج (هذا الملف)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><b>05_troubleshooting.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل</td></tr>
  </tbody>
</table>

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**