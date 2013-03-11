package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)


func sayhelloName(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()       //解析参数，默认是不会解析的
	fmt.Println(r.Form) //这些信息是输出到服务器端的打印信息
	fmt.Println("path", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
		fmt.Println("key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "Hello astaxie!") //这个写入到w的是输出到客户端的
}

func showNews(w http.ResponseWriter, r *http.Request) { 
    fmt.Fprintf(w, "hello\n")
}

func main() {
	http.HandleFunc("/hello", sayhelloName)       //设置访问的路由
	http.HandleFunc("/news", showNews)         // login
    err := http.ListenAndServe(":8888", http.FileServer(http.Dir("/root/scrapy/newsspider/pngs/")))
	//err := http.ListenAndServe("0.0.0.0:8888", nil) //设置监听的端口, 默认获取handler = DefaultServeMux
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
