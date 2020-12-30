from fillin import print_cat_by_mkp, fill_subcategories, print_subcat_by_cat, mkp_list, cat_list, print_marketplaces
from flask import Flask, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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


    #mkp_list = fill_marketplaces()
    mkp_list = print_marketplaces()

    for mkp in mkp_list:
        temp = {'nome': mkp.get_name(), 'rota': '/categorias/'+str(mkp.id)}
        print(temp)
        lista.append(temp)

    return render_template('index.html', nome=titulo_app, lista=lista )


@app.route("/categorias/<int:id>", methods=["GET"])
def categorias(id):
    listinha = []

    lista = print_cat_by_mkp(cat_list, id)

    titulo_app = "Categorias"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '/subcategorias/'+str(cat.id)}
        print(temp)
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )


@app.route("/subcategorias/<int:id>", methods=["GET"])
def subcategorias(id):
    listinha = []

    #subcat_list = fill_subcategories()
    lista = print_subcat_by_cat(cat_list, id)

    titulo_app = "Subategorias"

    for cat in lista:
        temp = {'nome': cat.get_name(), 'rota': '#'}
        listinha.append(temp)

    return render_template('index.html', nome=titulo_app, lista=listinha )


app.run(debug=True) 
