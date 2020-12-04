from flask import Flask, render_template, request
from tasador_app import Property

#Initialize variables
app = Flask(__name__, static_url_path="/tmp", static_folder="tmp")
app.secret_key = "" #Flask ask me for a key.

#Funcion predictora
def prediccion(propiedad):
    return [propiedad.rooms,
            propiedad.bedrooms,
            propiedad.bathrooms,
            propiedad.surface_total,
            propiedad.surface_covered,
            round(propiedad.predictValue())
            ]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# --- Tasador

@app.route('/tasar')
def tasador_page():
    return render_template('tasar.html')


@app.route('/tasar', methods=['POST'])
def tasar_prop():
    try:
        rooms = int(request.form['rooms'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        surface_total = int(request.form['sup_total'])
        surface_covered = int(request.form['sup_cub'])
        propiedad = Property(rooms, bedrooms, bathrooms, surface_total, surface_covered)
    except Exception as e:
        print(e)
        return render_template('/error.html')  # No queria lidiar con errores ni nada fancy
    print(propiedad)
    print(round(propiedad.predictValue()))
    prediction = prediccion(propiedad)
    return render_template('/prediction.html', prediction=prediction)

@app.route('/about')
def about_page():
    return render_template('about.html')


# Run main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
