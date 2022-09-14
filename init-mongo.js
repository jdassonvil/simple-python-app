conn = new Mongo();
db = conn.getDB("simplon");

db.messages.insert({text: "Hello Simplon !"});
db.messages.insert({text: "Hello World !"});
