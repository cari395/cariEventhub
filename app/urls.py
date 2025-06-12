from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/login/", views.login_view, name="login"),

    #Eventos
    path("events/", views.events, name="events"),
    path("events/create/", views.event_form, name="event_form"),
    path("events/<int:id>/edit/", views.event_form, name="event_edit"),
    path("events/<int:id>/", views.event_detail, name="event_detail"),
    path("events/<int:id>/delete/", views.event_delete, name="event_delete"),

    #CATEGORIAS
    path("categories/", views.category_list, name="category_list"),
    path("categories/new/", views.category_form, name="category_new"),
    path("categories/<int:id>/edit/", views.category_form, name="category_edit"),
    path("categories/<int:id>/delete/", views.category_delete, name="category_delete"),
    path('categories/<int:id>/events/', views.category_events, name='category_events'),

    #Tickets
    path("tickets", views.tickets, name="tickets"), # Ver tickets comprados siendo un cliente
    path("ticket/<int:id>/form/", views.ticket_form, name="ticket_form"), # El formulario de tarjeta de credito
    path("ticket/<str:ticket_code>/delete/", views.ticket_delete, name="ticket_delete"), # El formulario de tarjeta de credito
    path("ticket/<int:eventId>/buy/", views.ticket_buy, name="ticket_buy"), # El POST para comprar tickets

    path("ticket/<str:ticket_code>/edit/", views.ticket_edit, name="ticket_edit"), 

    path("ticket/<str:ticket_code>/form/edit", views.ticket_edit_form, name="ticket_edit_form"), # El POST para comprar tickets

    path('events/<int:event_id>/comment/add/', views.add_comment, name='add_comment'),# ruta para comentario
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comentario/<int:comment_id>/', views.view_comment, name='view_comment'),
    path('organizer/comments/', views.organizer_comments, name='organizer_comments'),
    path('reembolso/solicitar/', views.solicitar_reembolso, name='solicitar_reembolso'),
    path('refund/request/', views.solicitar_reembolso, name='solicitar_reembolso'),
    path('refund/myrefund/', views.my_refund, name='my_refund'),
    path('refund/edit/<int:id>/', views.editar_reembolso, name='editar_reembolso'),
    path('refund/delete/<int:id>/', views.eliminar_reembolso, name='eliminar_reembolso'),
    path('reembolsos/', views.reembolsos_eventos, name='reembolsos_eventos'),
    path('reembolsos/aprobar/<int:refund_id>/', views.aprobar_reembolso, name='aprobar_reembolso'),
    path('reembolsos/rechazar/<int:refund_id>/', views.rechazar_reembolso, name='rechazar_reembolso'),

    path('event/<int:event_id>/rating/create/', views.create_rating, name='create_rating'),
    path('event/<int:event_id>/rating/<int:rating_id>/update/', views.update_rating, name='update_rating'),
    path('event/<int:event_id>/rating/<int:rating_id>/delete/', views.delete_rating, name='delete_rating'),
    path('event/<int:event_id>/ratings/', views.list_ratings, name='list_ratings'),
    path('event/<int:event_id>/countdown/', views.countdown_json, name='countdown_json'),


## Venue
    path("venue/", views.venue, name="venue"),
    path("venue/create/", views.venue_form, name="venue_form"),
    path("venue/<int:id>/delete/", views.venue_baja, name="venue_delete"),
    path("venue/<int:id>/edit/", views.venue_form, name="venue_edit"),
    path("venue/<int:id>/", views.venue_detail, name="venue_detail"),

# encuesta
    path("survey/<str:ticket_code>/", views.satisfaction_survey, name="satisfaction_survey"),

]
