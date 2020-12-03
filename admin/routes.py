from app import app
from flask import render_template,request,url_for
@app.route('/admin')
def admin_index():
      return render_template('/admin/index.html')


@app.route('/admin/qallagenspotlar')
def admin_qalspot():
      return render_template('/admin/qalspots.html')

@app.route('/admin/lampalar')
def admin_lampa():
      return render_template('/admin/lampalar.html')

@app.route('/admin/create')
def admin_create():
      return render_template('/admin/create.html')

@app.route('/admin/update')
def admin_update():
      return render_template('/admin/update.html')

