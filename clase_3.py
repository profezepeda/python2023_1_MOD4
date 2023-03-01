class Producto():
    sku: str
    descripcion: str
    costo_pmp: float
    precio_venta: int
    productos: list = []

    def __init__(self, sku, descripcion, costo_pmp, precio_venta, productos):
        self.sku = sku
        self.descripcion = descripcion
        self.costo_pmp = costo_pmp
        self.precio_venta = precio_venta
        self.productos = productos

    def ingresar():
        pass
    
    def salir():
        pass
    
    def mermar():
        pass
    

pata1:Producto = Producto('1', 'Pata', 1000, 2000, [])
pata2:Producto = Producto('2', 'Pata', 1000, 2000, [])
pata3:Producto = Producto('3', 'Pata', 1000, 2000, [])
pata4:Producto = Producto('4', 'Pata', 1000, 2000, [])
cubierta:Producto = Producto('5', 'Cubierta', 1000, 2000, [])
mesa:Producto = Producto('6', 'Mesa', 1000, 2000, [
    pata1, pata2, pata3, pata4, cubierta
])