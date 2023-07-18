from .models import User, InteractionLog, WritingPlan, Administrator
from .database import db

# Operaciones CRUD para el modelo User

def create_user(username, password, contact_info):
    new_user = User(username=username, password=password, contact_info=contact_info)
    db.session.add(new_user)
    db.session.commit()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_all_users():
    return User.query.all()

def update_user(user_id, username=None, password=None, contact_info=None):
    user = get_user_by_id(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        if contact_info:
            user.contact_info = contact_info
        db.session.commit()

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()


# Operaciones CRUD para el modelo InteractionLog

def create_interaction_log(user_id, user_input, ai_feedback):
    new_log = InteractionLog(user_id=user_id, user_input=user_input, ai_feedback=ai_feedback)
    db.session.add(new_log)
    db.session.commit()

def get_interaction_log_by_id(log_id):
    return InteractionLog.query.get(log_id)

def get_all_interaction_logs():
    return InteractionLog.query.all()

def update_interaction_log(log_id, user_input=None, ai_feedback=None):
    log = get_interaction_log_by_id(log_id)
    if log:
        if user_input:
            log.user_input = user_input
        if ai_feedback:
            log.ai_feedback = ai_feedback
        db.session.commit()

def delete_interaction_log(log_id):
    log = get_interaction_log_by_id(log_id)
    if log:
        db.session.delete(log)
        db.session.commit()


# Operaciones CRUD para el modelo WritingPlan

def create_writing_plan(user_id, title, topic, communicative_intent, goal, central_idea, audience, status):
    new_plan = WritingPlan(user_id=user_id, title=title, topic=topic, communicative_intent=communicative_intent,
                           goal=goal, central_idea=central_idea, audience=audience, status=status)
    db.session.add(new_plan)
    db.session.commit()

def get_writing_plan_by_id(plan_id):
    return WritingPlan.query.get(plan_id)

def get_all_writing_plans():
    return WritingPlan.query.all()

def update_writing_plan(plan_id, title=None, topic=None, communicative_intent=None, goal=None, central_idea=None,
                        audience=None, status=None):
    plan = get_writing_plan_by_id(plan_id)
    if plan:
        if title:
            plan.title = title
        if topic:
            plan.topic = topic
        if communicative_intent:
            plan.communicative_intent = communicative_intent
        if goal:
            plan.goal = goal
        if central_idea:
            plan.central_idea = central_idea
        if audience:
            plan.audience = audience
        if status:
            plan.status = status
        db.session.commit()

def delete_writing_plan(plan_id):
    plan = get_writing_plan_by_id(plan_id)
    if plan:
        db.session.delete(plan)
        db.session.commit()


# Operaciones CRUD para el modelo Administrator

def create_administrator(name, password, contact_info):
    new_admin = Administrator(name=name, password=password, contact_info=contact_info)
    db.session.add(new_admin)
    db.session.commit()

def get_administrator_by_id(admin_id):
    return Administrator.query.get(admin_id)

def get_all_administrators():
    return Administrator.query.all()

def update_administrator(admin_id, name=None, password=None, contact_info=None):
    admin = get_administrator_by_id(admin_id)
    if admin:
        if name:
            admin.name = name
        if password:
            admin.password = password
        if contact_info:
            admin.contact_info = contact_info
        db.session.commit()

def delete_administrator(admin_id):
    admin = get_administrator_by_id(admin_id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
