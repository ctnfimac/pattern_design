"""
  Patrón Builder:
  Es un patrón de diseño creacional que nos permite construir objetos complejos
  paso a paso.
 
  El patrón nos permite producir distintos tipos y representaciones
  de un objeto empleando el mismo código de construcción.
 
   Es útil cuando necesitamos construir un objeto complejo con muchas partes
   y queremos que el proceso de construcción sea independiente de las partes
   que lo componen.
"""

"""
//! Tarea: crear un QueryBuilder para construir consultas SQL

  Debe de tener los siguientes métodos:
  - constructor(table: string)
  - select(fields: string[]): QueryBuilder -- si no se pasa ningún campo, se seleccionan todos con el  )
  - where(condition: string): QueryBuilder - opcional
  - orderBy(field: string, order: string): QueryBuilder - opcional
  - limit(limit: number): QueryBuilder - opcional
  - execute(): string - retorna la consulta SQL
  
  Ejemplo de uso:
  const usersQuery = new QueryBuilder("users") // users es el nombre de la tabla
    .select("id", "name", "email")
    .where("age > 18")
    .where("country = 'Cri'")
    .orderBy("name", "ASC")
    .limit(10)
    .execute();

  console.log('Consulta: ', usersQuery);
  // Select id, name, email from users where age > 18 and country = 'Cri' order by name ASC limit 10;
"""

class Query:

    def __init__(self):
        self.select: str = ""
        self.where: list = []
        self.order_by: str = ""
        self.limit: str = ""
        self.table: str = ""

    
    def __str__(self):
        response = "SELECT "
        response += self.select if self.select else " * "
        response += f" FROM {self.table}" if self.table else ""

        #for condition in self.where:
        if len(self.where) > 1:
            dato = " AND ".join(self.where)
            response += f" WHERE {dato}"
        else:
            response += f" WHERE {self.where}" if self.where else ""
        response += f" ORDER_BY {self.order_by}" if self.order_by else ""
        response += f" LIMIT {self.limit}" if self.limit else ""
        return response
    

class QueryBuilder:
    _query: None

    def __init__(self, table:str):
        self._query = Query()
        self._query.table = table

    def select(self, select:list) -> "QueryBuilder":
        self._query.select = ", ".join(select)
        return self

    def where(self, condition:str) -> "QueryBuilder":
        self._query.where.append(condition)
        return self
    
    def order_by(self, field:str="id", type:str="ASC") -> "QueryBuilder":
        self._query.order_by = f"{field} {type}"
        return self

    def limit(self, limit:int) -> "QueryBuilder":
        self._query.limit = limit
        return self
    
    def build(self) -> Query:
        return self._query
    

if __name__ == "__main__":
    usersQuery = QueryBuilder("users")\
        .select(["id", "name", "email"])\
        .where("age > 18")\
        .where("country = 'Cri'")\
        .order_by("name", "ASC")\
        .limit(10)\
        .build()

    print(f'Consulta: {usersQuery}')

    usersQueryAll = QueryBuilder("markers")\
        .select(["*"])\
        .order_by("email", "DESC")\
        .build()

    print(f'Consulta: {usersQueryAll}')