# SGR-dev2
# Desarrollo tecnológico

# Problematica:

La problemática central de este proyecto gira sobre modelos tecnológicos que faciliten el desarrollo del pensamiento científico en niños y niñas ente 5 y 10 años que se encuentran en zonas de baja conectividad a Internet. Se ha hablado desde hace mucho tiempo sobre tutores inteligentes, pero los desarrollos han sido lentos y el acceso muy costoso para la mayoría de la población en el planeta. Sin embargo, desarrollos recientes sobre PNL han permitido que tecnologías como ChatGPT puedan presentar alternativas a esta problemática. Es así que se espera contar con una solución tecnológica que para permita fortalecer las capacidades de escritura en temas relacionados con ciencias naturales en la población seleccionada. Dicha solución se basará en el motor de ChatGPT 4.0 y en dos desarrollos pedagógicos y didácticos de varios profesores de la Universidad Icesi. El primer desarrollo consiste en un conjunto de secuencias didácticas en ciencias naturales que son apoyadas por cuentos como mecanismo de enganche y que pueden ser fácilmente aplicables en cualquier contexto educativo (Ref: proyecto maría isable rivas). **El segundo desarrollo pedagógico** corresponde a un modelo para redactar un plan de escritura y oralidad con IA. Con estos tres componentes se espera ofrecer a niños y niñas una herramienta digital que les permita entender temas relacionados con ciencias naturales y proponer un plan de escritura como herramienta para explicitar ese entendimiento.

# Estructura para la implementación del proyecto

### **Front-end**:

1. Página de inicio
    - Ingreso/Registro de usuarios
    - Información del proyecto
    - Enlace a página de ayuda
2. Área de usuario
    - Sección de tema
    - Sección de intención comunicativa
    - Sección de objetivo/meta
    - Sección de idea central/mensaje central
    - Sección de auditorio/audiencia
3. Panel de retroalimentación de IA
    - Cuadro de diálogo para interacciones con IA
4. Página de ayuda y soporte
    - Guías de usuario
    - FAQ
5. Panel de administración (acceso restringido)
    - Visualización de logs
    - Administración de usuarios

### **Back-end**:

1. Módulo de autenticación de usuarios
    - Registro de usuarios
    - Ingreso de usuarios
2. Módulo de interacción con IA
    - Generación de diálogo
    - Proporcionar retroalimentación
3. Módulo de administración
    - Generación de logs
    - Visualización de logs para administradores
    - Administración de usuarios
4. Módulo de ayuda y soporte
    - Mantenimiento de FAQ
    - Actualizaciones y anuncios

### **Base de datos**:

1. Tabla de usuarios
    - ID de usuario
    - Nombre de usuario
    - Contraseña (hash)
    - Información de contacto
    - Fecha de creación del usuario
2. Tabla de logs de interacciones
    - ID de log
    - ID de usuario
    - Fecha y hora de interacción
    - Entrada de usuario
    - Retroalimentación de IA
3. Tabla de planes de escritura/oralidad
    - ID del plan
    - ID de usuario
    - Título del plan
    - TEMA
    - INTENCIÓN COMUNICATIVA
    - OBJETIVO o META
    - IDEA CENTRAL O MENSAJE CENTRAL
    - AUDITORIO / AUDIENCIA
    - Estado del plan (borrador, finalizado, etc.)
4. Tabla de administradores
    - ID de administrador
    - Nombre de administrador
    - Contraseña (hash)
    - Información de contacto
# Uso
```
pip install -r requirements.txt
export FLASK_APP=backend/app
flask db init
flask db migrate
flask db upgrade

flask run
```
# Caracteristicas

1. **Estructura de la página web**: La página debe tener una interfaz de usuario (front-end) amigable, intuitiva y atractiva. La página podría dividirse en diferentes secciones que representan cada uno de los cinco aspectos del plan de escritura/oralidad. Los usuarios podrán ingresar a cada sección, recibir orientación de la IA, y escribir sus respuestas.
2. **Interacción con la IA**: El usuario podría interactuar con la IA (GPT) a través de un cuadro de diálogo. La IA podría hacer preguntas para guiar al usuario a través del proceso de desarrollo de cada aspecto del plan.
3. **Almacenamiento y acceso a logs**: Las interacciones con la IA deben ser almacenadas en un servidor o base de datos (back-end). El acceso a estos registros debe estar restringido a los administradores, quienes podrían utilizar un panel de control protegido por contraseña para ver y analizar los logs.
4. **Feedback en tiempo real**: Basándose en las respuestas de los usuarios, la IA podría proporcionar feedback en tiempo real para ayudar a los usuarios a mejorar sus respuestas y a desarrollar sus habilidades de escritura.
5. **Guía de ayuda y soporte**: La página web debe tener una sección de ayuda y soporte con tutoriales, consejos y respuestas a preguntas frecuentes para ayudar a los usuarios a utilizar la herramienta de manera efectiva.
6. **Actualizaciones y mejoras**: Se debe tener un mecanismo para recibir feedback de los usuarios y realizar mejoras y actualizaciones periódicas en la página web y en la IA.
7. **Seguridad y privacidad**: La página web debe cumplir con todas las leyes y regulaciones aplicables de privacidad y protección de datos. Los usuarios deben ser informados sobre cómo se recogen, almacenan y utilizan sus datos.
8. **Optimización de la IA**: Con el tiempo, los administradores podrían utilizar los logs para entender cómo los usuarios interactúan con la IA y para mejorar y optimizar la IA basándose en esta información.
9. **Adaptabilidad a dispositivos móviles**: Asegúrate de que la página web esté optimizada para dispositivos móviles para permitir el acceso en cualquier lugar y en cualquier momento.

# Consideraciones

1. **Adaptabilidad del contenido**: Asegúrar que el contenido sea adecuado para niños y niñas de 5 a 10 años. Esto incluye la simplicidad del lenguaje y la interactividad de la interfaz.
2. **Interfaz amigable para niños**: El diseño de la interfaz debe ser atractivo y fácil de usar para los niños. Los botones y las instrucciones deben ser grandes y claros, y el lenguaje debe ser simple.
3. **Modo Offline**: Como mencionamos anteriormente, para áreas con baja conectividad, es necesario tener un modo offline que permita a los niños interactuar con la aplicación sin necesidad de una conexión constante a Internet. Esto podría implicar el almacenamiento local de ciertos datos y la sincronización de estos datos con la base de datos principal cuando haya conexión disponible.
4. **Contenido descargable**: Para minimizar la necesidad de conectividad, puedes proporcionar contenido que se pueda descargar cuando haya conexión disponible y que luego se pueda utilizar offline. Esto podría incluir lecciones, ejercicios y retroalimentación de la IA.

# La guia para niños

1. **Mi súper idea (TEMA)**: Este es el gran pensamiento que tienes en tu cabeza, ¡es sobre lo que quieres hablar! Podría ser sobre tu mascota, tu superhéroe favorito, o ese delicioso helado que comiste el otro día. Solo recuerda, es como el título de tu historia: "La increíble aventura de mi perro Max".
2. **Lo que quiero hacer (INTENCIÓN COMUNICATIVA)**: Este es el 'por qué' de tu historia. ¿Quieres hacer reír a tus amigos con una historia súper divertida? ¿O tal vez quieres compartir algo interesante que aprendiste en la escuela? Aquí decides lo que quieres lograr con tu historia, es como tu misión secreta.
3. **Mi objetivo (OBJETIVO o META)**: ¿Qué te gustaría que tus amigos hagan o sientan después de escuchar tu historia? ¿Te gustaría que aprendan algo nuevo, que se rían mucho o que se sorprendan con tu historia? Aquí decides el efecto mágico de tu historia en tus amigos.
4. **El corazón de mi historia (IDEA CENTRAL O MENSAJE CENTRAL)**: ¿Cuál es la idea más importante de tu historia? ¡El secreto que quieres compartir con el mundo! Podría ser: "Incluso un pequeño ratón puede ser un gran héroe", o "Los helados de vainilla son los más deliciosos del mundo".
5. **Para quién es mi historia (AUDITORIO / AUDIENCIA)**: ¿Quién crees que disfrutaría más de tu historia? Podrían ser tus amigos del colegio, tu mamá y papá, o incluso tu profesora. Decides a quién le gustaría más tu historia, como elegir el mejor regalo para alguien que aprecias.

```
proyecto/
|--- backend/
|    |--- __init__.py
|    |--- run.py
|    |--- app/
|    |    |--- __init__.py
|    |    |--- auth/
|    |    |    |--- __init__.py
|    |    |    |--- routes.py
|    |    |    |--- forms.py
|    |    |    |--- models.py
|    |    |--- interaction/
|    |    |    |--- __init__.py
|    |    |    |--- routes.py
|    |    |    |--- forms.py
|    |    |    |--- models.py
|    |    |--- admin/
|    |    |    |--- __init__.py
|    |    |    |--- routes.py
|    |    |    |--- forms.py
|    |    |    |--- models.py
|    |    |--- support/
|    |    |    |--- __init__.py
|    |    |    |--- routes.py
|    |    |    |--- forms.py
|    |    |    |--- models.py
|    |    |--- common/
|    |    |    |--- __init__.py
|    |    |    |--- utils.py
|    |    |--- templates/
|    |    |--- static/
|    |--- database/
|    |    |--- __init__.py
|    |    |--- models.py
|    |    |--- database.py
|    |    |--- crud.py
|--- frontend/
|    |--- public/
|    |    |--- index.html
|    |--- src/
|    |    |--- main.js
|    |    |--- App.vue
|    |    |--- components/
|    |    |--- assets/
|    |    |--- router/
|    |    |--- store/
```
