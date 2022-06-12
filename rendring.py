from flask import *  
app = Flask(__name__)  
 
@app.route('/message/<var>')  
def message(var):  
      return render_template('about.html', name = var)  

if __name__ == '__main__':  
   app.run(debug = True)