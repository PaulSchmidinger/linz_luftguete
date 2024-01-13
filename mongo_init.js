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
