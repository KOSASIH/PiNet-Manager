// blockchain_management_api.rs
#[macro_use]
extern crate rocket;
extern crate diesel;

use rocket::response::content;
use rocket_contrib::json::Json;

mod models {
    use diesel::prelude::*;
    use diesel::sqlite::SqliteConnection;

    #[derive(Queryable, Serialize)]
    pub struct Block {
        id: i32,
        hash: String,
        previous_hash: String,
        timestamp: i64,
        data: String,
    }
}

mod schema {
    use diesel::prelude::*;

    table! {
        blocks (id) {
            id -> Integer,
            hash -> VarChar,
            previous_hash -> VarChar,
            timestamp -> BigInt,
            data -> Text,
        }
    }
}

#[post("/blocks", data = "<block>")]
fn create_block(block: Json<models::Block>) -> Json<models::Block> {
    let conn = establish_connection();
    diesel::insert_into(schema::blocks::table)
       .values(&block)
       .execute(&conn)
       .unwrap();
    Json(block)
}

#[get("/blocks")]
fn get_blocks() -> Json<Vec<models::Block>> {
    let conn = establish_connection();
    let blocks = schema::blocks::table.load::<models::Block>(&conn).unwrap();
    Json(blocks)
}

fn establish_connection() -> SqliteConnection {
    SqliteConnection::establish("blockchain.db").unwrap()
}

fn main() {
    rocket::ignite()
       .mount("/", routes![create_block, get_blocks])
       .launch();
}
