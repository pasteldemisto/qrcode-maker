import qrcode

# Gera o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://<BOTA-O-LINK-AQUI>/')
qr.make(fit=True)

# Salva a imagem
img = qr.make_image(fill_color="black", back_color="white")
img.save('NOME-IMAGEM.png')