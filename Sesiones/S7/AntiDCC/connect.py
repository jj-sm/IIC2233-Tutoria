def setup_conexiones(cliente, admin, backend):
    # Cliente vota -> Backend recibe voto
    cliente.senal_votar.connect(backend.recibir_voto)
    # Admin inicia conteo -> Backend inicia conteo
    admin.senal_iniciar_conteo.connect(backend.iniciar_conteo)
    # Backend manda resultado -> Admin actualiza
    backend.senal_resultado_conteo.connect(admin.actualizar_conteo)
    # Backend manda estado -> Cliente actualiza
    backend.senal_estado_conteo.connect(cliente.actualizar_estado)
    # Backend manda monitoreo -> Admin actualiza monitoreo
    backend.senal_monitoreo_conteo.connect(admin.actualizar_monitoreo)