# 📊 البيانات المستخدمة | Dataset Documentation

> **توثيق كامل لمجموعة بيانات UNSW-NB15 والـ 49 عموداً**

---

## 🎯 نظرة عامة

مجموعة بيانات **UNSW-NB15** هي مجموعة بيانات أكاديمية معيارية تم إنشاؤها بواسطة **UNSW Canberra Cyber Range Lab** في أستراليا. تُستخدم على نطاق واسع في أبحاث **Network Intrusion Detection Systems (NIDS)** وتطبيقات **Machine Learning for Cybersecurity**.

تم تصميم المجموعة لتوفير بيانات واقعية عن حركة الشبكة، تشمل **Traffic عادي** و **Traffic خبيث** من **9 فئات هجمات** مختلفة.

---

## 📌 معلومات أساسية

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">اسم Dataset</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المصدر</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW Canberra Cyber Range Lab, Australia</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">سنة الإنشاء</td><td style="padding: 8px; border: 1px solid #ddd;">2015</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحجم الكلي</td><td style="padding: 8px; border: 1px solid #ddd;">~642 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد الملفات</td><td style="padding: 8px; border: 1px solid #ddd;">7 CSV Files</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد السجلات</td><td style="padding: 8px; border: 1px solid #ddd;">2,540,047 سجل (بعد المعالجة)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد الأعمدة</td><td style="padding: 8px; border: 1px solid #ddd;">49 عموداً (48 features + 1 label)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الرابط الرسمي</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="https://research.unsw.edu.au/projects/unsw-nb15-dataset">UNSW-NB15 Dataset</a></td></tr>
  </tbody>
</table>

---

## 📁 الملفات المكونة للـ Dataset

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">اسم الملف</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الحجم</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_1.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~162 MB</td><td style="padding: 8px; border: 1px solid #ddd;">الملف الأساسي الأول</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_2.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~158 MB</td><td style="padding: 8px; border: 1px solid #ddd;">الملف الأساسي الثاني</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_3.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~148 MB</td><td style="padding: 8px; border: 1px solid #ddd;">الملف الأساسي الثالث</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_4.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~94 MB</td><td style="padding: 8px; border: 1px solid #ddd;">الملف الأساسي الرابع</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_GT.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~83 MB</td><td style="padding: 8px; border: 1px solid #ddd;">Ground Truth Labels</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_features.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~4 KB</td><td style="padding: 8px; border: 1px solid #ddd;">وصف الأعمدة الـ 49</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_LIST_EVENTS.csv</td><td style="padding: 8px; border: 1px solid #ddd;">~4.6 KB</td><td style="padding: 8px; border: 1px solid #ddd;">قائمة الأحداث</td></tr>
  </tbody>
</table>

> **ملاحظة:** الملفات **4 الأساسية** (`_1` إلى `_4`) هي مصدر البيانات الرئيسي. الملفات الثلاثة الأخرى مساعدة (Ground Truth، Feature Description، Events List).

---

## 🗂️ الـ 49 عموداً

تحتوي مجموعة البيانات على **49 عموداً** (48 feature + 1 label). تم تقسيمها إلى **5 فئات رئيسية**:

### 1. Flow Features

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Feature</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النوع</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">srcip</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Source IP Address</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">sport</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source Port Number</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">dstip</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Destination IP Address</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">dsport</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Port Number</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">proto</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Transaction Protocol</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">state</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Connection State</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">dur</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Total Duration</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">sbytes</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source to Destination Bytes</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">dbytes</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination to Source Bytes</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">sttl</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source TTL</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">11</td><td style="padding: 8px; border: 1px solid #ddd;">dttl</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination TTL</td></tr>
  </tbody>
</table>

### 2. Basic Features

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Feature</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النوع</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">12</td><td style="padding: 8px; border: 1px solid #ddd;">sloss</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source Packets Lost</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">13</td><td style="padding: 8px; border: 1px solid #ddd;">dloss</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Packets Lost</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">14</td><td style="padding: 8px; border: 1px solid #ddd;">service</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Service (http, ftp, dns, ...)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">15</td><td style="padding: 8px; border: 1px solid #ddd;">Sload</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Source Bits per Second</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">16</td><td style="padding: 8px; border: 1px solid #ddd;">Dload</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Bits per Second</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">17</td><td style="padding: 8px; border: 1px solid #ddd;">Spkts</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source Packet Count</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">18</td><td style="padding: 8px; border: 1px solid #ddd;">Dpkts</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Packet Count</td></tr>
  </tbody>
</table>

### 3. TCP Features

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Feature</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النوع</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">19</td><td style="padding: 8px; border: 1px solid #ddd;">swin</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source TCP Window</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">20</td><td style="padding: 8px; border: 1px solid #ddd;">dwin</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination TCP Window</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">21</td><td style="padding: 8px; border: 1px solid #ddd;">stcpb</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source TCP Base Sequence</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">22</td><td style="padding: 8px; border: 1px solid #ddd;">dtcpb</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination TCP Base Sequence</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">23</td><td style="padding: 8px; border: 1px solid #ddd;">smeansz</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Mean Source Packet Size</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">24</td><td style="padding: 8px; border: 1px solid #ddd;">dmeansz</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Mean Destination Packet Size</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">25</td><td style="padding: 8px; border: 1px solid #ddd;">trans_depth</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">HTTP Transaction Depth</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">26</td><td style="padding: 8px; border: 1px solid #ddd;">res_bdy_len</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Response Body Length</td></tr>
  </tbody>
</table>

### 4. Time Features

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Feature</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النوع</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">27</td><td style="padding: 8px; border: 1px solid #ddd;">Sjit</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Source Jitter (mSec)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">28</td><td style="padding: 8px; border: 1px solid #ddd;">Djit</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Jitter (mSec)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">29</td><td style="padding: 8px; border: 1px solid #ddd;">Stime</td><td style="padding: 8px; border: 1px solid #ddd;">Timestamp</td><td style="padding: 8px; border: 1px solid #ddd;">Record Start Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">30</td><td style="padding: 8px; border: 1px solid #ddd;">Ltime</td><td style="padding: 8px; border: 1px solid #ddd;">Timestamp</td><td style="padding: 8px; border: 1px solid #ddd;">Record Last Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">31</td><td style="padding: 8px; border: 1px solid #ddd;">Sintpkt</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Source Interpacket Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">32</td><td style="padding: 8px; border: 1px solid #ddd;">Dintpkt</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Interpacket Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">33</td><td style="padding: 8px; border: 1px solid #ddd;">tcprtt</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">TCP Round Trip Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">34</td><td style="padding: 8px; border: 1px solid #ddd;">synack</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">SYN to SYN_ACK Time</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">35</td><td style="padding: 8px; border: 1px solid #ddd;">ackdat</td><td style="padding: 8px; border: 1px solid #ddd;">Float</td><td style="padding: 8px; border: 1px solid #ddd;">SYN_ACK to ACK Time</td></tr>
  </tbody>
</table>

### 5. Additional Features

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Feature</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">النوع</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">36</td><td style="padding: 8px; border: 1px solid #ddd;">is_sm_ips_ports</td><td style="padding: 8px; border: 1px solid #ddd;">Binary</td><td style="padding: 8px; border: 1px solid #ddd;">Same IP/Port Indicator</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">37</td><td style="padding: 8px; border: 1px solid #ddd;">ct_state_ttl</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Count by State + TTL</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">38</td><td style="padding: 8px; border: 1px solid #ddd;">ct_flw_http_mthd</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">HTTP Methods Count</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">39</td><td style="padding: 8px; border: 1px solid #ddd;">is_ftp_login</td><td style="padding: 8px; border: 1px solid #ddd;">Binary</td><td style="padding: 8px; border: 1px solid #ddd;">FTP Login Indicator</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">40</td><td style="padding: 8px; border: 1px solid #ddd;">ct_ftp_cmd</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">FTP Commands Count</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">41</td><td style="padding: 8px; border: 1px solid #ddd;">ct_srv_src</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Service + Source Connections</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">42</td><td style="padding: 8px; border: 1px solid #ddd;">ct_srv_dst</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Service + Destination Connections</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">43</td><td style="padding: 8px; border: 1px solid #ddd;">ct_dst_ltm</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Destination Connections</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">44</td><td style="padding: 8px; border: 1px solid #ddd;">ct_src_ltm</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source Connections</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">45</td><td style="padding: 8px; border: 1px solid #ddd;">ct_src_dport_ltm</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source + Dest Port</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">46</td><td style="padding: 8px; border: 1px solid #ddd;">ct_dst_sport_ltm</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Dest + Source Port</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">47</td><td style="padding: 8px; border: 1px solid #ddd;">ct_dst_src_ltm</td><td style="padding: 8px; border: 1px solid #ddd;">Integer</td><td style="padding: 8px; border: 1px solid #ddd;">Source + Dest IP</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">48</td><td style="padding: 8px; border: 1px solid #ddd;">attack_cat</td><td style="padding: 8px; border: 1px solid #ddd;">Nominal</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Category (9 classes)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">49</td><td style="padding: 8px; border: 1px solid #ddd;">Label</td><td style="padding: 8px; border: 1px solid #ddd;">Binary</td><td style="padding: 8px; border: 1px solid #ddd;">0 = Normal, 1 = Attack</td></tr>
  </tbody>
</table>

---

## 🛡️ فئات الهجمات (9 Classes)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الفئة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Generic</td><td style="padding: 8px; border: 1px solid #ddd;">تقنيات تُحاكي أساليب هجوم محددة، وتُطبَّق بشكل عام على أنظمة متعددة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Exploits</td><td style="padding: 8px; border: 1px solid #ddd;">استغلال ثغرات معروفة في الأنظمة والخدمات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Fuzzers</td><td style="padding: 8px; border: 1px solid #ddd;">إرسال بيانات عشوائية لاختبار الأنظمة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">DoS</td><td style="padding: 8px; border: 1px solid #ddd;">Denial of Service - تعطيل الخدمة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">Reconnaissance</td><td style="padding: 8px; border: 1px solid #ddd;">عمليات استطلاع لجمع معلومات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">Analysis</td><td style="padding: 8px; border: 1px solid #ddd;">تحليل حركة الشبكة والبيانات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">Backdoors</td><td style="padding: 8px; border: 1px solid #ddd;">إنشاء أبواب خلفية للوصول غير المصرح</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">Shellcode</td><td style="padding: 8px; border: 1px solid #ddd;">كود خبيث يُنفَّذ داخل النظام</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">Worms</td><td style="padding: 8px; border: 1px solid #ddd;">ديدان تنتشر تلقائياً عبر الشبكة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">—</td><td style="padding: 8px; border: 1px solid #ddd;">Normal</td><td style="padding: 8px; border: 1px solid #ddd;">حركة شبكة طبيعية (ليست هجمة)</td></tr>
  </tbody>
</table>

---

## 📊 توزيع البيانات بعد المعالجة

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
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Attacks</td><td style="padding: 8px; border: 1px solid #ddd;">321,283</td><td style="padding: 8px; border: 1px solid #ddd;">12.65%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Total</b></td><td style="padding: 8px; border: 1px solid #ddd;"><b>2,540,047</b></td><td style="padding: 8px; border: 1px solid #ddd;"><b>100%</b></td></tr>
  </tbody>
</table>

---

## 📌 ملاحظات مهمة

### 1. Feature Types
- **Nominal (String):** srcip, dstip, proto, state, service, attack_cat.
- **Integer:** معظم الحقول الرقمية.
- **Float:** dur, Sload, Dload, Sjit, Djit.
- **Binary:** is_sm_ips_ports, is_ftp_login, Label.
- **Timestamp:** Stime, Ltime.

### 2. القيم الناقصة
- ممثلة بـ `-` في CSV.
- يتم تحويلها إلى `null` في Spark.
- تشمل: `service`, `attack_cat`, وبعض الحقول الرقمية.

### 3. القيم الشاذة (Outliers)
- تظهر Outliers في: `dur`, `sbytes`, `dbytes`.
- قد ترتبط ببعض أنماط DoS أو بحالات شبكة غير معتادة.
- لا تتم معالجتها في هذه المرحلة، لأنها قد تمثّل سلوكاً فعلياً للهجمات.

### 4. Data Imbalance
- **87% Normal** vs **13% Attack**.
- **التأثير:** يحتاج ML Models معالجة خاصة (Class Weighting).

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
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;"><b>02_dataset.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">البيانات (هذا الملف)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><b>03_pipeline.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><b>04_results.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><b>05_troubleshooting.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل</td></tr>
  </tbody>
</table>

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**