DROP TABLE IF EXISTS 問題;

CREATE TABLE 問題 (
  問題番号 INTEGER NOT NULL PRIMARY KEY,
  問題文 TEXT NOT NULL,
  正答 TEXT NOT NULL,
  選択肢 TEXT NOT NULL
);

DROP TABLE IF EXISTS 回答履歴;

CREATE TABLE 回答履歴 (
  問題番号 INTEGER NOT NULL REFERENCES 問題(問題番号),
  回答 TEXT NOT NULL,
  日付 DATE NOT NULL
);

INSERT INTO 問題(問題番号, 問題文, 正答, 選択肢)
VALUES
  (1, "蘇我氏が滅ぼされ、大化の改新が始まったのは何年？", "645", "645,654,564,546"),
  (2, "遣唐使を廃止したのは何年？", "894", "894,849,948,984"),
  (3, "都を平城京に遷都したのは何年？", "710", "710,794,749,770"),
  (4, "都を平安京に遷都したのは何年？", "794", "794,710,765,724"),
  (5, "平等院鳳凰堂が建設されたのは何年？", "1053", "1053,1035,1305,1003"),

  (6, "平清盛が大政大臣になったのは何年？", "1167", "1167,1176,1192,1185"),
  (7, "壇ノ浦の戦いで平氏が滅びたのは何年？", "1185", "1185,1158,1167,1176"),
  (8, "承久の乱が起きたのは何年？", "1221", "1221,1122,1212,1224"),
  (9, "足利尊氏が幕府を開いたのは何年？", "1338", "1338,1383,1333,1316"),
  (10, "応仁の乱が起きたのは何年？", "1467", "1467,1476,1647,1444"),

  (11, "織田信長が室町幕府を滅ぼしたのは何年？", "1573", "1573,1357,1537,1567"),
  (12, "豊臣秀吉が全国を統一したのは何年？", "1590", "1590,1580,1599,1690"),
  (13, "関ヶ原の戦いが起こったのは何年？", "1600", "1600,1610,1666,1616"),
  (14, "徳川家康が幕府を開いたのは何年？", "1603", "1603,1630,1613,1623"),
  (15, "徳川慶喜が政権を朝廷に返したのは何年？", "1867", "1867,1768,1876,1786"),

  (16, "福澤諭吉が『学問のすゝめ』を書いたのは何年？", "1872", "1872,1782,1727,1777"),
  (17, "大日本帝国憲法が発布されたのは何年？", "1889", "1889,1898,1899,1888"),
  (18, "普通選挙制度が差がめられたのは何年？", "1925", "1925,1935,1923,1920"),
  (19, "太平洋戦争が起きたのは何年？", "1941", "1941,1955,1945,1935"),
  (20, "日本国憲法が公布されたのは何年？", "1946", "1946,1945,1950,1955"),

  (21, "日米安全保障条約を結んだのは何年？", "1951", "1951,1961,1955,1960"),
  (22, "日本が国際連合に加盟したのは何年？", "1956", "1956,1965,1960,1963"),
  (23, "沖縄が日本に返還されたのは何年？", "1972", "1972,1982,1977,1987"),
  (24, "日中平和和友好条約を結んだのは何年？", "1978", "1978,1987,1967,1976"),
  (25, "藩が廃止され県が置かれたのは何年？", "1871", "1871,1877,1880,1887")
  ;