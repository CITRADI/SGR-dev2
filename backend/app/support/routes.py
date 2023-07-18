from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from support import support_bp
from support.forms import SupportForm
from support.models import FAQ

@support_bp.route('/support', methods=['GET', 'POST'])
@login_required
def support():
    form = SupportForm()
    if form.validate_on_submit():
        # Lógica para manejar los datos del formulario y guardar en la base de datos
        faq = FAQ(question=form.question.data, answer=form.answer.data)
        faq.save()
        
        flash('FAQ agregado con éxito.', 'success')
        return redirect(url_for('home'))

    return render_template('support.html', form=form)
