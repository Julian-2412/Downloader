import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp
import os

def descargar_video():

    
    progreso.pack(pady=5)
    label_progreso.pack(pady=5)
        

    link = entry_link.get()
    seleccion = opciones_var.get()
    ruta = entry_ruta.get().strip()
    descargar = descargar_sino_var.get()
    miniatura = opciones_video_var.get()
    informacion = opciones_video_informacion_var.get()
    anotaciones = opciones_video_anotaciones_var.get()
    subtitulos = opciones_video_subtitulos_var.get()
    idioma = opciones_video_idioma_var.get()
    descripcion = opciones_video_descripcion_var.get()
    video_format = opciones_video_formato_var.get()
    auido_format = opciones_video_Audioformato_var.get()
    audio_calidad = opciones_video_Audioformato_calidad_var.get()
    calidad_video = opciones_video_calidad_var.get()

    if not ruta.endswith(os.sep):
        ruta += os.sep

    ruta_final = ruta + '%(title)s.%(ext)s'

    ydl_opts = {
        'outtmpl' : ruta_final,
        'extractor_args': {'youtube': {'geo_bypass': True}},
        'progress_hooks': [progress_hook]
    }

    if (descargar == "Si"):
        descargar = True
    elif(descargar == "No"):
        descargar = False
    
    ydl_opts['postprocessors'] = []

    # if auido_format == "mp3":
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegExtractAudio',  
    #     'preferredcodec': 'mp3',      
    #     'preferredquality': audio_calidad,    
    # })
    # elif auido_format == "aac":  
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegExtractAudio',  
    #     'preferredcodec': 'aac',      
    #     'preferredquality': audio_calidad,    
    # })
    # elif auido_format == "FLAC":  
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegExtractAudio',  
    #     'preferredcodec': 'flac',      
    #     'preferredquality': audio_calidad,    
    # })
    # elif auido_format == "WAV":  
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegExtractAudio',  
    #     'preferredcodec': 'wav',      
    #     'preferredquality': audio_calidad,    
    # })
    # elif auido_format == "OGG":  
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegExtractAudio',  
    #     'preferredcodec': 'ogg',      
    #     'preferredquality': audio_calidad,    
    # })

    # if video_format == "MP4":
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegVideoConvertor',    
    #     'preferedformat': 'mp4',          
    # })
    # elif video_format == "MKV":
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegVideoConvertor',   
    #     'preferedformat': 'mkv',          
    # })
    # elif video_format == "AVI":
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegVideoConvertor',   
    #     'preferedformat': 'avi',          
    # })
    # elif video_format == "WEBM":
    #     ydl_opts['postprocessors'].append({
    #     'key': 'FFmpegVideoConvertor',   
    #     'preferedformat': 'webm',          
    # })


    if subtitulos == "Si":
        ydl_opts['writesubtitles'] = subtitulos
        ydl_opts['subtitleslangs'] = [idioma]
        ydl_opts['subtitlesformat'] = 'srt' 
        ydl_opts['subtitle'] = True  

    if descripcion == "Si":
        ydl_opts['writedescription'] = descripcion

    if anotaciones == "Si":
        #ydl_opts['write_annotations'] = anotaciones
        messagebox.showwarning("Advertencia", "Las anotaciones de YouTube fueron eliminadas en 2019 y no se pueden descargar.")

    if informacion == "Si":
        ydl_opts['writeinfojson'] = informacion

    if miniatura == "Si":
        ydl_opts['writethumbnail'] = miniatura


    # if seleccion == "Audio":
    #     ydl_opts['format'] = 'bestaudio'
    # elif seleccion == "Video":
    #     ydl_opts['format'] = f'bestvideo[height<={calidad_video}]+bestaudio/best[height<={calidad_video}]'
    # elif seleccion == "Video sin sonido":
    #     ydl_opts['format'] = f'bestvideo[height={calidad_video}]'

    # Limpia postprocesadores previos

    if seleccion == "Audio":
        # Configuración exclusiva para Audio
        ydl_opts['format'] = 'bestaudio'
        
        if auido_format:  # Si se especifica un formato de audio
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': auido_format.lower(),  # Formato de audio (en minúsculas)
                'preferredquality': audio_calidad
            })

    elif seleccion == "Video":
        # Configuración exclusiva para Video
        ydl_opts['format'] = f'bestvideo[height<={calidad_video}]+bestaudio/best[height<={calidad_video}]'
        
        if video_format:  # Si se especifica un formato de video
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegVideoConvertor',
                'preferedformat': video_format.lower()  # Formato de video (en minúsculas)
            })

    elif seleccion == "Video sin sonido":
        # Configuración para video sin audio
        ydl_opts['format'] = f'bestvideo[height<={calidad_video}]'

        if video_format:  # Si se especifica un formato de video
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegVideoConvertor',
                'preferedformat': video_format.lower()  # Formato de video (en minúsculas)
            })

    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download = descargar, force_generic_extractor = True)
        

        #crea un label dónde más adelante se muestra la información del video de yt
            #crea un label para separación
        label_separacion = tk.Label(frame_contenido, text = "", justify = "left")
        label_separacion.pack(pady = 10)

            #crea el label de titulo
        label_titulo = tk.Label(frame_contenido, text="", justify="left")
        label_titulo.pack(pady=10)

            #creacion label de la url de la imagen
        label_imagen = tk.Label(frame_contenido, text="", justify="left")
        label_imagen.pack(pady = 10)

            #crea el label de la descripcción
        label_descripcion = tk.Label(frame_contenido, text="", justify="left")
        label_descripcion.pack(pady=10)

            #crea el label de la fecha de subida 
        label_fecha = tk.Label(frame_contenido, text="", justify="left")
        label_fecha.pack(pady=10)

            #crea el label del que subió el video
        label_subidopor = tk.Label(frame_contenido, text="", justify="left")
        label_subidopor.pack(pady=10)

            #crea el label de la duración del video, en segundo
        label_duracion = tk.Label(frame_contenido, text="", justify="left")
        label_duracion.pack(pady=10)


        label_separacion.config(text = f"------------------------------------------------------------------------------------------")
        label_titulo.config(text = f"Título \n{info.get('title')}\n")
        label_imagen.config(text = f"Url de la minuatura \n{info.get('thumbnail')}\n")
        label_descripcion.config(text =  f"Descripción \n{info.get('description')}\n")                        
        label_fecha.config(text =  f"Fecha de subida \n{info.get('upload_date')}\n")                            
        label_subidopor.config(text = f"Subido por \n{info.get('uploader')}\n")                            
        label_duracion.config(text = f"Duración \n{info.get('duration')} segundos")                  

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar el video: {e}")


def actualizar_opciones(*args):

    if descargar_sino_var.get() == "Si":
        frame_opciones.pack(before = btn_descargar, pady=5)
        frame_opciones_video.pack(before = btn_descargar, pady = 5)
        frame_opciones_video_informacion.pack(before = btn_descargar, pady = 5)
        frame_opciones_video_anotaciones.pack(before = btn_descargar, pady = 5)
        frame_opciones_video_subtitulos.pack(before = btn_descargar, pady = 5)
        frame_opciones_video_descripcion.pack(before = btn_descargar, pady = 5)

        if opciones_video_subtitulos_var.get() == "Si":
            frame_opciones_video_idioma.pack(before = frame_opciones_video_descripcion, pady = 5)

        else:
            frame_opciones_video_idioma.pack_forget()
            opciones_video_idioma_var.set("en")

        if opciones_var.get() == "Video" or  opciones_var.get() == "Video sin sonido":
            frame_opciones_video_formato.pack(before = btn_descargar, pady = 5)
            frame_opciones_video_Audioformato.pack_forget()
            opciones_video_formato_var.set("MP4")
            opciones_video_Audioformato_var.set("N/A")
            frame_opciones_video_Audioformato_calidad.pack_forget()
            opciones_video_Audioformato_calidad_var.set("N/A")
            frame_opciones_video_calidad.pack(before = btn_descargar, pady = 5)
            opciones_video_calidad_var.set(1080)

        elif opciones_var.get() == "Audio":
            opciones_video_formato_var.set("N/A")
            frame_opciones_video_formato.pack_forget()

            frame_opciones_video_Audioformato.pack(before = btn_descargar, pady = 5)
            opciones_video_Audioformato_var.set("MP3")

            frame_opciones_video_Audioformato_calidad.pack(before = btn_descargar, pady = 5)
            opciones_video_Audioformato_calidad_var.set("320")

            frame_opciones_video_calidad.pack_forget()
            opciones_video_calidad_var.set(0)




    else:
        frame_opciones.pack_forget()
        opciones_var.set("Video")

        frame_opciones_video.pack_forget()
        opciones_video_var.set("No") 

        frame_opciones_video_informacion.pack_forget()
        opciones_video_informacion_var.set("No")

        frame_opciones_video_anotaciones.pack_forget()
        opciones_video_anotaciones_var.set("No") 

        frame_opciones_video_subtitulos.pack_forget()
        opciones_video_subtitulos_var.set("No")

        frame_opciones_video_descripcion.pack_forget()
        opciones_video_descripcion_var.set("No")




def progress_hook(d):
  
    
    if d['status'] == 'downloading':
        # Calcular el progreso en porcentaje
        porcentaje = int(d['downloaded_bytes'] * 100 / d['total_bytes'])
        
        # Actualizar la barra de progreso
        progreso["value"] = porcentaje
        label_progreso.config(text=f"Progreso: {porcentaje}%")
        ventana.update_idletasks()  # Refrescar la interfaz
        btn_descargar.config(bg = "green")

    elif d['status'] == 'finished':
        # Cuando termine la descarga y el mensaje no haya sido mostrado
        label_progreso.config(text="Descarga completada!")
        messagebox.showinfo("Completado", "El archivo se descargó correctamente, pero aun falta procesar el video, espera que el botón vuelva a ser rojo")
        btn_descargar.config(bg = "red")

        
#crear la ventana   
ventana = tk.Tk()
ventana.title("Descargador de Videos YouTube")
ventana.geometry("500x400")


#crear el label dónde irá el link
label_link = tk.Label(ventana, text="Link")
label_link.pack()
entry_link = tk.Entry(ventana, width = 40)
entry_link.pack(pady = 5)


#crear el label dónde irá el ruta de descarga
label_ruta = tk.Label(ventana, text = "Ruta dónde almacenar")
label_ruta.pack()
entry_ruta = tk.Entry(ventana, width = 40)
entry_ruta.pack(pady = 5)


#crear el label dónde irá un menú desplegable para saber si se va a descargar o no
label_descargar = tk.Label(ventana, text = "¿Descargar?")
label_descargar.pack(pady = 5)
descargar_sino =  ["Si", "No"]
descargar_sino_var = tk.StringVar()
descargar_sino_var.set(descargar_sino[1])
    
    #"inicializar" el menú
menu_desplegable_sino = tk.OptionMenu(ventana, descargar_sino_var, *descargar_sino)
menu_desplegable_sino.pack(pady = 5)
    
        #agregar la función a la supervicion 
descargar_sino_var.trace("w", actualizar_opciones)

#crear el label dónde irá un menú para saber que cosa va a descargar
frame_opciones = tk.Frame(ventana)
label_opciones = tk.Label(frame_opciones, text = "Tipo de archivo")
label_opciones.pack(side = 'left')
opciones = ["Video", "Audio", "Video sin sonido"]
opciones_var = tk.StringVar()
opciones_var.set(opciones[0])
     
     #"inicializar" el menú
menu_desplegable_archivo = tk.OptionMenu(frame_opciones, opciones_var, *opciones)
menu_desplegable_archivo.pack()
    
    #agregar la función a la supervición
opciones_var.trace("w", actualizar_opciones)

#crear un frame y label dónde irá la opción de descargar la miniatura
frame_opciones_video = tk.Frame(ventana)
label_opciones_video = tk.Label(frame_opciones_video, text = "¿Descargar miniatura?")
label_opciones_video.pack(side = 'left')
opciones_video = ["Si", "No"]
opciones_video_var = tk.StringVar()
opciones_video_var.set(opciones_video[1])

    #inicializar el menú
menu_desplegable_archivo_descargar_miniatura = tk.OptionMenu(frame_opciones_video, opciones_video_var, *opciones_video)
menu_desplegable_archivo_descargar_miniatura.pack()


#crear un frame y label para saber si quiere guardar la información del video
frame_opciones_video_informacion = tk.Frame(ventana)
label_opciones_video_informacion = tk.Label(frame_opciones_video_informacion, text = "¿Guardar la información del video?")
label_opciones_video_informacion.pack(side = 'left')
opciones_video_informacion = ["Si", "No"]
opciones_video_informacion_var = tk.StringVar()
opciones_video_informacion_var.set(opciones_video_informacion[1])

    #inicializar el menú
menu_desplegable_archivo_descargar_informacion = tk.OptionMenu(frame_opciones_video_informacion, opciones_video_informacion_var, *opciones_video_informacion)
menu_desplegable_archivo_descargar_informacion.pack()


#crea un frame y un label para poder saber si quiere descargar als anotaciones de un video
frame_opciones_video_anotaciones =  tk.Frame(ventana)
label_opciones_video_anotaciones = tk.Label(frame_opciones_video_anotaciones, text = "¿Guardar anotaciones del video?")
label_opciones_video_anotaciones.pack(side = 'left')
opciones_video_anotaciones = ["Si", "No"]
opciones_video_anotaciones_var = tk.StringVar()
opciones_video_anotaciones_var.set(opciones_video_anotaciones[1])

    #inicializar el menú
menu_desplegable_archivo_descargar_anotaciones = tk.OptionMenu(frame_opciones_video_anotaciones, opciones_video_anotaciones_var, *opciones_video_anotaciones)
menu_desplegable_archivo_descargar_anotaciones.pack() 


#crear otro frame y label para saber si descargar los subtitulos o no
frame_opciones_video_subtitulos = tk.Frame(ventana)
label_opciones_video_subtitulos = tk.Label(frame_opciones_video_subtitulos, text = "¿Guardar subtitulos del video?")
label_opciones_video_subtitulos.pack(side = 'left')
opciones_video_subtitulos = ["Si", "No"]
opciones_video_subtitulos_var = tk.StringVar()
opciones_video_subtitulos_var.set(opciones_video_subtitulos[1])

    #inicializar el menu
menu_desplegable_archivo_descargar_subtitulos = tk.OptionMenu(frame_opciones_video_subtitulos, opciones_video_subtitulos_var, *opciones_video_subtitulos)
menu_desplegable_archivo_descargar_subtitulos.pack()

    #relacionar función con el método 
opciones_video_subtitulos_var.trace("w", actualizar_opciones)


#crear el frame y el label para el idioma
frame_opciones_video_idioma = tk.Frame(ventana)
label_opciones_video_idioma = tk.Label(frame_opciones_video_idioma, text = "¿En que idioma?")
label_opciones_video_idioma.pack(side = 'left')
opciones_video_idioma = ["en", "es"]
opciones_video_idioma_var = tk.StringVar()
opciones_video_idioma_var.set(opciones_video_idioma[1])

    #inicializar menú
menu_desplegable_archivo_descargar_idioma = tk.OptionMenu(frame_opciones_video_idioma, opciones_video_idioma_var, *opciones_video_idioma)
menu_desplegable_archivo_descargar_idioma.pack() 


#crear el frame y el label para descargar la descripción del video
frame_opciones_video_descripcion = tk.Frame(ventana)
label_opciones_video_descripcion = tk.Label(frame_opciones_video_descripcion, text = "¿Guardar descripción?")
label_opciones_video_descripcion.pack(side = 'left')
opciones_video_descripcion = ["Si", "No"]
opciones_video_descripcion_var = tk.StringVar()
opciones_video_descripcion_var.set(opciones_video_descripcion[1])

    #inicializar menú
menu_desplegable_archivo_descargar_descripcion = tk.OptionMenu(frame_opciones_video_descripcion, opciones_video_descripcion_var, *opciones_video_descripcion)
menu_desplegable_archivo_descargar_descripcion.pack() 


#crear un frame y label para saber que tipo de formato de video descargar 
frame_opciones_video_formato = tk.Frame(ventana)
label_opciones_video_formato = tk.Label(frame_opciones_video_formato, text = "¿Que tipo de formato?")
label_opciones_video_formato.pack(side = 'left') 
opciones_video_formato = ["MP4", "MKV", "AVI", "WEBM"]
opciones_video_formato_var = tk.StringVar()
opciones_video_formato_var.set(opciones_video_formato[0])

    #inicializar menú
menu_desplegable_archivo_descargar_formato = tk.OptionMenu(frame_opciones_video_formato, opciones_video_formato_var, *opciones_video_formato)
menu_desplegable_archivo_descargar_formato.pack()


#crear ahora el frame y el label para el tipo de formato de los auidos
frame_opciones_video_Audioformato = tk.Frame(ventana)
label_opciones_video_Audioformato = tk.Label(frame_opciones_video_Audioformato, text = "¿Que tipo de formato?")
label_opciones_video_Audioformato.pack(side = 'left')
opciones_video_Audioformato = ["mp3", "aac", "flac", "wav", "ogg"]
opciones_video_Audioformato_var = tk.StringVar()
opciones_video_Audioformato_var.set(opciones_video_Audioformato[0])

    #inicializar el menú
menu_desplegable_archivo_descargar_Auidioformato = tk.OptionMenu(frame_opciones_video_Audioformato, opciones_video_Audioformato_var, *opciones_video_Audioformato)
menu_desplegable_archivo_descargar_Auidioformato.pack()


#frmae y label para la calidad del audio
frame_opciones_video_Audioformato_calidad = tk.Frame(ventana)
label_opciones_video_Audioformato_calidad = tk.Label(frame_opciones_video_Audioformato_calidad, text = "¿Calidad?")
label_opciones_video_Audioformato_calidad.pack(side = 'left')
opciones_video_Audioformato_calidad = [128, 192, 256, 320]
opciones_video_Audioformato_calidad_var = tk.StringVar()
opciones_video_Audioformato_calidad_var.set(opciones_video_Audioformato_calidad[3])

    #inicializar el menú
menu_desplegable_archivo_descargar_Auidioformato_calidad = tk.OptionMenu(frame_opciones_video_Audioformato_calidad, opciones_video_Audioformato_calidad_var, *opciones_video_Audioformato_calidad)
menu_desplegable_archivo_descargar_Auidioformato_calidad.pack()


#frame y label para calidad de video
frame_opciones_video_calidad = tk.Frame(ventana)
label_opciones_video_calidad = tk.Label(frame_opciones_video_calidad, text = "¿Calidad?")
label_opciones_video_calidad.pack(side = 'left') 
opciones_video_calidad = [2160, 1440, 1080, 720, 480, 360, 240, 144]
opciones_video_calidad_var = tk.StringVar()
opciones_video_calidad_var.set(opciones_video_calidad[2])

    #inicializar menú
menu_desplegable_archivo_descargar_video_calidad = tk.OptionMenu(frame_opciones_video_calidad, opciones_video_calidad_var, *opciones_video_calidad)
menu_desplegable_archivo_descargar_video_calidad.pack()


#crea el botón final de descarga y llama la función dónde se hace ese proceso
btn_descargar = tk.Button(ventana, text="Descargar", command=descargar_video, bg="red")
btn_descargar.pack(pady=20)


#se crea el frame con scroll para mostrar la información 
frame_scroll = tk.Frame(ventana)
frame_scroll.pack(expand=True, fill="both", pady=10)

canvas = tk.Canvas(frame_scroll)
scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
frame_contenido = tk.Frame(canvas) 

    # Configurar el canvas
frame_contenido.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

    # Empaquetar canvas y scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

label_progreso = tk.Label(frame_contenido, text="Progreso: 0%", justify="left")
label_progreso.pack_forget()
progreso = ttk.Progressbar(frame_contenido, length=300, mode="determinate")
progreso.pack_forget()


ventana.mainloop()
