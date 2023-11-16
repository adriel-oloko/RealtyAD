CREATE TABLE listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_hash TEXT,
    list_address TEXT,
    list_street TEXT,
    list_area TEXT,
    list_state TEXT,
    list_price TEXT,
    list_property_type TEXT,
    list_building_type TEXT,
    list_bedroom TEXT,
    list_bathroom TEXT,
    list_toilet TEXT,
    list_parking TEXT,
    list_added_date TEXT,
    list_status TEXT,
    list_img TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    p_id TEXT,
    link TEXT
);