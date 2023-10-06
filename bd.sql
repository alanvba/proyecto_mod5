
INSERT INTO public.ejeapp_tipo_hoja_ruta (id, descripcion, estado) VALUES (1, 'Interna', true);
INSERT INTO public.ejeapp_tipo_hoja_ruta (id, descripcion, estado) VALUES (2, 'Externa', true);

INSERT INTO public.ejeapp_usuario (id, usuario, passwords, nombres, apellidos, estado, created, updated) VALUES (1, 'Alan', '123', 'Alan', 'vasquez', true, '2023-10-03 23:29:14.236874-04', '2023-10-03 23:29:14.236874-04');

INSERT INTO public.ejeapp_hoja_ruta (id, numero, remitente, referencia, fechahora, created, updated, tipohoja_ruta_id, prioritario) VALUES (1, 1, 'Claudia', 'Solicitud de certificacion de curso', '2023-10-03 23:33:41.919836-04', '2023-10-03 23:33:41.919836-04', '2023-10-03 23:33:41.919836-04', 1, true);

INSERT INTO public.ejeapp_remision (id, idusuario_origen, idusuario_destino, estado, habilitado, created, updated, hoja_ruta_id) VALUES (1, 1, 1, 'ev', true, '2023-10-03 23:34:05.827802-04', '2023-10-03 23:34:05.827802-04', 1);
