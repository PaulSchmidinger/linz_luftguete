db.createUser({
    user: "envuser",
    pwd: "envpass",
    roles: [
        {
            role: "readWrite",
            db: "mydatabase"
        }
    ]
});

// Create indexes on relevant fields for optimized queries
db.linz_collection.createIndex({ "zeitpunkt": 1 });
db.linz_collection.createIndex({ "station": 1 });
db.linz_collection.createIndex({ "komponente": 1 });
db.linz_collection.createIndex({ "mittelwert": 1 });
