// node_management_api.go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type Node struct {
	gorm.Model
	Name     string `json:"name"`
	IPAddress string `json:"ip_address"`
	Status   string `json:"status"`
}

var db *gorm.DB
var err error

func main() {
	db, err = gorm.Open("sqlite3", "./node_management.db")
	if err!= nil {
		fmt.Println("Error opening database:", err)
		return
	}
	defer db.Close()

	db.AutoMigrate(&Node{})

	r := mux.NewRouter()
	r.HandleFunc("/nodes", getNodes).Methods("GET")
	r.HandleFunc("/nodes", createNode).Methods("POST")
	r.HandleFunc("/nodes/{id}", getNode).Methods("GET")
	r.HandleFunc("/nodes/{id}", updateNode).Methods("PUT")
	r.HandleFunc("/nodes/{id}", deleteNode).Methods("DELETE")

	http.ListenAndServe(":8000", r)
}

func getNodes(w http.ResponseWriter, r *http.Request) {
	var nodes []Node
	db.Find(&nodes)
	json.NewEncoder(w).Encode(&nodes)
}

func createNode(w http.ResponseWriter, r *http.Request) {
	var node Node
	_ = json.NewDecoder(r.Body).Decode(&node)
	db.Create(&node)
	json.NewEncoder(w).Encode(&node)
}

func getNode(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	var node Node
	db.First(&node, params["id"])
	json.NewEncoder(w).Encode(&node)
}

func updateNode(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	var node Node
	db.First(&node, params["id"])
	_ = json.NewDecoder(r.Body).Decode(&node)
	db.Save(&node)
	json.NewEncoder(w).Encode(&node)
}

func deleteNode(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	var node Node
	db.First(&node, params["id"])
	db.Delete(&node)
	json.NewEncoder(w).Encode(&node)
}
