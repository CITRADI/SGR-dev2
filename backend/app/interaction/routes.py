from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from interaction import interaction_bp
from interaction.forms import InteractionForm
from interaction.models import Interaction
from common.utils import generate_response_from_gpt

@interaction_bp.route('/interaction', methods=['GET', 'POST'])
@login_required
def interaction():
    form = InteractionForm()
    if form.validate_on_submit():
        input_text = form.input_text.data
        
        # Llamada a la función para generar la respuesta utilizando ChatGPT
        response_text = generate_response_from_gpt(input_text)
        
        # Guardar la interacción en la base de datos
        interaction = Interaction(input_text=input_text, response_text=response_text, user_id=current_user.id)
        interaction.save()
        
        flash('Interacción guardada con éxito.', 'success')
        return redirect(url_for('home'))

    return render_template('interaction.html', form=form)
