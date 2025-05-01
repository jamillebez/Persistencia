from pydantic import BaseModel, Field, root_validator

class Livro(BaseModel):
    id: int = Field(gt=0, description="ID deve ser maior que zero")
    titulo: str
    autor: str
    ano: int
    genero: str

    @root_validator(pre=True)
    def check_for_invalid_values(cls, values):
        for field, value in values.items():
            if value == "string" or value == "":
                raise ValueError(f'O campo "{field}" não pode ser vazio ou conter o valor "string".')
            
        id_value = values.get("id")
        if id_value is not None and id_value <= 0:
            raise ValueError('O campo "id" deve ser maior que zero.')

        ano_value = values.get("ano")
        if ano_value is not None and ano_value <= 0:
            raise ValueError('O campo "ano" deve ser maior que zero.')
        
        return values

    class Config:
        title = "Livro"
        anystr_strip_whitespace = True  
