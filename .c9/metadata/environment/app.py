{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":62,"position":62,"stack":[[{"start":{"row":13,"column":12},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":40},"action":"insert","lines":["books=mongo.db.books.find().limit(8)"],"id":23}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"remove","lines":["8"],"id":24},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["2"]}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":[","],"id":25}],[{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":[" "],"id":26},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["b"]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["o"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["o"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["k"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["s"]},{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["b"],"id":27},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["o"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["o"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["k"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["s"],"id":28}],[{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"remove","lines":["s"],"id":29}],[{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"remove","lines":["s"],"id":31}],[{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":40},"action":"remove","lines":[" book=mongo.db.books.find().limit(2)"],"id":33},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":12},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"remove","lines":["k"],"id":34},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"remove","lines":["o"]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"remove","lines":["o"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["b"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["="]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":["k"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"remove","lines":["o"]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"remove","lines":["o"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"remove","lines":["b"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"remove","lines":[" "]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"remove","lines":[","]}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["4"],"id":35},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["1"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["2"]}],[{"start":{"row":33,"column":38},"end":{"row":33,"column":39},"action":"remove","lines":["8"],"id":36},{"start":{"row":33,"column":38},"end":{"row":33,"column":39},"action":"insert","lines":["1"]},{"start":{"row":33,"column":39},"end":{"row":33,"column":40},"action":"insert","lines":["2"]}],[{"start":{"row":46,"column":8},"end":{"row":46,"column":49},"action":"remove","lines":["'rating':int(request.form.get('rating')),"],"id":37},{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"remove","lines":["    "]},{"start":{"row":45,"column":46},"end":{"row":46,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":49},"action":"remove","lines":["'rating':int(request.form.get('rating')),"],"id":38},{"start":{"row":60,"column":4},"end":{"row":60,"column":8},"action":"remove","lines":["    "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "]},{"start":{"row":59,"column":46},"end":{"row":60,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":52,"column":0},"end":{"row":64,"column":41},"action":"remove","lines":["","@app.route('/update_book/<book_id>', methods=[\"POST\"])","def update_book(book_id):","    book = mongo.db.books","    book.update( {'_id': ObjectId(book_id)},","    {","        'title': request.form.get('title'),","        'authors':request.form.get('authors'),","        'language_code':request.form.get('language_code'),","        'isbn13':int(request.form.get('isbn13')),","        'num_pages':int(request.form.get('num_pages'))","    })","    return redirect(url_for('get_books'))"],"id":39}],[{"start":{"row":51,"column":41},"end":{"row":52,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":57,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":41}],[{"start":{"row":58,"column":0},"end":{"row":70,"column":41},"action":"insert","lines":["","@app.route('/update_book/<book_id>', methods=[\"POST\"])","def update_book(book_id):","    book = mongo.db.books","    book.update( {'_id': ObjectId(book_id)},","    {","        'title': request.form.get('title'),","        'authors':request.form.get('authors'),","        'language_code':request.form.get('language_code'),","        'isbn13':int(request.form.get('isbn13')),","        'num_pages':int(request.form.get('num_pages'))","    })","    return redirect(url_for('get_books'))"],"id":42}],[{"start":{"row":70,"column":41},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":48,"column":8},"end":{"row":48,"column":54},"action":"remove","lines":["'num_pages':int(request.form.get('num_pages'))"],"id":44}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":8},"action":"remove","lines":["    "],"id":45},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "]},{"start":{"row":47,"column":49},"end":{"row":48,"column":0},"action":"remove","lines":["",""]},{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"remove","lines":[","]}],[{"start":{"row":46,"column":58},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":46},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":54},"action":"insert","lines":["'num_pages':int(request.form.get('num_pages'))"],"id":47}],[{"start":{"row":47,"column":54},"end":{"row":47,"column":55},"action":"insert","lines":[","],"id":48}],[{"start":{"row":66,"column":58},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":67,"column":0},"end":{"row":67,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":67,"column":8},"end":{"row":67,"column":54},"action":"insert","lines":["'num_pages':int(request.form.get('num_pages'))"],"id":50}],[{"start":{"row":67,"column":54},"end":{"row":67,"column":55},"action":"insert","lines":[","],"id":51}],[{"start":{"row":69,"column":8},"end":{"row":69,"column":54},"action":"remove","lines":["'num_pages':int(request.form.get('num_pages'))"],"id":52},{"start":{"row":69,"column":4},"end":{"row":69,"column":8},"action":"remove","lines":["    "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"remove","lines":["    "]},{"start":{"row":68,"column":49},"end":{"row":69,"column":0},"action":"remove","lines":["",""]},{"start":{"row":68,"column":48},"end":{"row":68,"column":49},"action":"remove","lines":[","]}],[{"start":{"row":6,"column":21},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":53}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":120},"action":"remove","lines":["mongodb+srv://root:r00tUser@cluster0-y00j5.mongodb.net/goodreads?retryWrites=true&w=majority'"],"id":54},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["'"]}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["o"],"id":55},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["s"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["."]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["n"],"id":56},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["v"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["i"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["r"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["o"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["n"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":[","]}],[{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["g"],"id":57},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["e"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":40},"end":{"row":9,"column":42},"action":"insert","lines":["()"],"id":58}],[{"start":{"row":9,"column":41},"end":{"row":9,"column":43},"action":"insert","lines":["\"\""],"id":59}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":["M"],"id":60},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["O"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["N"]},{"start":{"row":9,"column":45},"end":{"row":9,"column":46},"action":"insert","lines":["G"]},{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"insert","lines":["O"]}],[{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"insert","lines":["_"],"id":61},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"insert","lines":["U"]},{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"insert","lines":["R"]},{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"insert","lines":["I"]}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"remove","lines":[","],"id":62}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["."],"id":63}],[{"start":{"row":57,"column":74},"end":{"row":58,"column":0},"action":"remove","lines":["",""],"id":64}],[{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"insert","lines":["."],"id":65},{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"insert","lines":["f"]},{"start":{"row":61,"column":27},"end":{"row":61,"column":28},"action":"insert","lines":["i"]},{"start":{"row":61,"column":28},"end":{"row":61,"column":29},"action":"insert","lines":["n"]},{"start":{"row":61,"column":29},"end":{"row":61,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":61,"column":26},"end":{"row":61,"column":30},"action":"remove","lines":["find"],"id":66},{"start":{"row":61,"column":26},"end":{"row":61,"column":34},"action":"insert","lines":["find_one"]}],[{"start":{"row":61,"column":34},"end":{"row":61,"column":36},"action":"insert","lines":["()"],"id":67}],[{"start":{"row":61,"column":35},"end":{"row":61,"column":37},"action":"insert","lines":["{}"],"id":68}],[{"start":{"row":61,"column":36},"end":{"row":61,"column":38},"action":"insert","lines":["\"\""],"id":69}],[{"start":{"row":61,"column":37},"end":{"row":61,"column":38},"action":"insert","lines":["_"],"id":70},{"start":{"row":61,"column":38},"end":{"row":61,"column":39},"action":"insert","lines":["i"]},{"start":{"row":61,"column":39},"end":{"row":61,"column":40},"action":"insert","lines":["d"]},{"start":{"row":61,"column":40},"end":{"row":61,"column":41},"action":"insert","lines":[":"]}],[{"start":{"row":61,"column":42},"end":{"row":61,"column":43},"action":"insert","lines":[":"],"id":71}],[{"start":{"row":61,"column":43},"end":{"row":61,"column":44},"action":"insert","lines":[" "],"id":72},{"start":{"row":61,"column":44},"end":{"row":61,"column":45},"action":"insert","lines":["O"]},{"start":{"row":61,"column":45},"end":{"row":61,"column":46},"action":"insert","lines":["b"]},{"start":{"row":61,"column":46},"end":{"row":61,"column":47},"action":"insert","lines":["j"]},{"start":{"row":61,"column":47},"end":{"row":61,"column":48},"action":"insert","lines":["e"]},{"start":{"row":61,"column":48},"end":{"row":61,"column":49},"action":"insert","lines":["c"]},{"start":{"row":61,"column":49},"end":{"row":61,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":61,"column":44},"end":{"row":61,"column":50},"action":"remove","lines":["Object"],"id":73},{"start":{"row":61,"column":44},"end":{"row":61,"column":52},"action":"insert","lines":["ObjectId"]}],[{"start":{"row":61,"column":52},"end":{"row":61,"column":54},"action":"insert","lines":["()"],"id":74}],[{"start":{"row":61,"column":53},"end":{"row":61,"column":54},"action":"insert","lines":["b"],"id":75},{"start":{"row":61,"column":54},"end":{"row":61,"column":55},"action":"insert","lines":["o"]}],[{"start":{"row":61,"column":53},"end":{"row":61,"column":55},"action":"remove","lines":["bo"],"id":76},{"start":{"row":61,"column":53},"end":{"row":61,"column":60},"action":"insert","lines":["book_id"]}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":45},"action":"remove","lines":["DESCENDING"],"id":78},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"remove","lines":[" "]},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"remove","lines":[","]}],[{"start":{"row":71,"column":4},"end":{"row":72,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]},{"start":{"row":72,"column":4},"end":{"row":73,"column":0},"action":"insert","lines":["",""]},{"start":{"row":73,"column":0},"end":{"row":73,"column":4},"action":"insert","lines":["    "]},{"start":{"row":73,"column":4},"end":{"row":73,"column":5},"action":"insert","lines":["k"]},{"start":{"row":73,"column":5},"end":{"row":73,"column":6},"action":"insert","lines":["j"]},{"start":{"row":73,"column":6},"end":{"row":73,"column":7},"action":"insert","lines":["y"]},{"start":{"row":73,"column":7},"end":{"row":73,"column":8},"action":"insert","lines":["u"]},{"start":{"row":73,"column":8},"end":{"row":73,"column":9},"action":"insert","lines":["k"]},{"start":{"row":73,"column":9},"end":{"row":73,"column":10},"action":"insert","lines":["u"]},{"start":{"row":73,"column":10},"end":{"row":73,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":73,"column":10},"end":{"row":73,"column":11},"action":"remove","lines":["y"],"id":80}],[{"start":{"row":73,"column":9},"end":{"row":73,"column":10},"action":"remove","lines":["u"],"id":81},{"start":{"row":73,"column":8},"end":{"row":73,"column":9},"action":"remove","lines":["k"]},{"start":{"row":73,"column":7},"end":{"row":73,"column":8},"action":"remove","lines":["u"]},{"start":{"row":73,"column":6},"end":{"row":73,"column":7},"action":"remove","lines":["y"]},{"start":{"row":73,"column":5},"end":{"row":73,"column":6},"action":"remove","lines":["j"]}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":5},"action":"remove","lines":["k"],"id":82},{"start":{"row":73,"column":0},"end":{"row":73,"column":4},"action":"remove","lines":["    "]},{"start":{"row":72,"column":4},"end":{"row":73,"column":0},"action":"remove","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "]},{"start":{"row":71,"column":4},"end":{"row":72,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":9},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":83}],[{"start":{"row":4,"column":9},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":84}],[{"start":{"row":75,"column":27},"end":{"row":75,"column":28},"action":"insert","lines":["d"],"id":85},{"start":{"row":75,"column":28},"end":{"row":75,"column":29},"action":"insert","lines":["d"]},{"start":{"row":75,"column":29},"end":{"row":75,"column":30},"action":"insert","lines":["d"]},{"start":{"row":75,"column":30},"end":{"row":75,"column":31},"action":"insert","lines":["d"]},{"start":{"row":75,"column":31},"end":{"row":75,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":75,"column":31},"end":{"row":75,"column":32},"action":"remove","lines":["d"],"id":86},{"start":{"row":75,"column":30},"end":{"row":75,"column":31},"action":"remove","lines":["d"]},{"start":{"row":75,"column":29},"end":{"row":75,"column":30},"action":"remove","lines":["d"]},{"start":{"row":75,"column":28},"end":{"row":75,"column":29},"action":"remove","lines":["d"]},{"start":{"row":75,"column":27},"end":{"row":75,"column":28},"action":"remove","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":790.5,"scrollleft":0,"selection":{"start":{"row":61,"column":63},"end":{"row":61,"column":63},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":48,"state":"start","mode":"ace/mode/python"}},"timestamp":1578959152310,"hash":"231a61480fd72e4e496da6749116a93dfe9c614f"}