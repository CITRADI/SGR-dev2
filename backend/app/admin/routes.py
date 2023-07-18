from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from admin import admin_bp
from admin.forms import AdminForm
from admin.models import Admin

@admin_bp.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        # Lógica para manejar los datos del formulario y guardar en la base de datos
        admin = Admin(name=form.name.data, password=form.password.data, email=form.email.data)
        admin.save()
        
        flash('Administrador creado con éxito.', 'success')
        return redirect(url_for('home'))

    return render_template('admin.html', form=form)
