from fillin import fill_marketplaces, fill_categories, print_cat_by_mkp, fill_subcategories, print_subcat_by_cat
from flask import Flask, render_template


app = Flask(__name__)


titulo_app = 'Marketplaces Olist'

#@app.route('/')
#def index():
#    h1 = '<h1>Listagem Marketplaces</h1>'
#    ol = '''
#            <ol>
#                
#         '''
#    mkp_list = fill_marketplaces()#
#
#    for mkp in mkp_list:
#        ol = ol + "<li><a href='/"+ mkp.get_name()+"'>"+str(mkp)+"</a></li>"
#
#    ol = ol + "</ol>"
#    return f'{h1} {ol}'


@app.route('/')
def index():
    lista = []


    mkp_list = fill_marketplaces()

    for mkp in mkp_list:
        temp = {'nome': mkp.get_name(), 'rota': '/'+mkp.get_name()}
        print(temp)
        lista.append(temp)

    return render_template('index.html', nome=titulo_app, lista=lista )


@app.route('/Americanas')
def americanas():
    listinha = []

    cat_list = fill_categories()
    lista = print_cat_by_mkp(cat_list, 2)

    titulo_app = "Categorias Americanas"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '/'+cat.get_name()}
        print(temp)
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )

@app.route('/Submarino')
def submarino():
    listinha = []

    cat_list = fill_categories()
    lista = print_cat_by_mkp(cat_list, 1)

    titulo_app = "Categorias Submarino"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '/'+cat.get_name()}
        print(temp)
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )

@app.route('/MercadoLivre')
def mercado():
    listinha = []

    cat_list = fill_categories()
    lista = print_cat_by_mkp(cat_list, 3)

    titulo_app = "Categorias Mercado Livre"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '/'+cat.get_name()}
        print(temp)
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )



@app.route('/Smartphones')
def smartphones():
    listinha = []

    subcat_list = fill_subcategories()
    lista = print_subcat_by_cat(subcat_list, 1)

    titulo_app = "Subategorias Smartphones"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '/'+cat.get_name()}
        print(temp)
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )




app.run(debug=True) 
