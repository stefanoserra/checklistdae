DROP TABLE IF EXISTS controlli;
DROP TABLE IF EXISTS sedi;

CREATE TABLE controlli (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sede VARCHAR(50),
    dispositivo VARCHAR(50),
    dataControllo DATE,
    operatore VARCHAR(50),
    piastreAdulto VARCHAR(10),
    piastrePediatriche VARCHAR(10),
    batteria VARCHAR(10),
    note TEXT
);

CREATE TABLE sedi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sede VARCHAR(50)
);

CREATE TABLE dispositivi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo VARCHAR(50)
);

INSERT INTO controlli (dataControllo, sede, dispositivo, operatore, piastreAdulto, piastrePediatriche, batteria, note) VALUES (
    '2021-12-10 12:05:03',
    'Pisa',
    'DAE001-PHILIPS',
    'Mario Rossi',
    'OK',
    'OK',
    'OK',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
);

INSERT INTO controlli (dataControllo, sede, dispositivo, operatore, piastreAdulto, piastrePediatriche, batteria, note) VALUES (
    '2022-01-15 15:45:53',
    'Riglione',
    'DAE017-PHILIPS',
    'Luigi Bianchi',
    'OK',
    'Non Ok',
    'OK',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
);

INSERT INTO sedi(sede) VALUES('Arena Metato');
INSERT INTO sedi(sede) VALUES('Asciano');
INSERT INTO sedi(sede) VALUES('Gello');
INSERT INTO sedi(sede) VALUES('Lungarno');
INSERT INTO sedi(sede) VALUES('Migliarino');
INSERT INTO sedi(sede) VALUES('Pisa');
INSERT INTO sedi(sede) VALUES('Pontasserchio');
INSERT INTO sedi(sede) VALUES('Riglione');
INSERT INTO sedi(sede) VALUES('San Giuliano Terme');

INSERT INTO dispositivi(dispositivo) VALUES('DAE-8374');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-2354');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-2675');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-2853');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-1847');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-0386');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-1746');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-2056');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-1047');
INSERT INTO dispositivi(dispositivo) VALUES('DAE-1853');