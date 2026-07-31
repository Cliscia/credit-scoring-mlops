"""Category labels for the South German Credit dataset."""

CATEGORY_MAPPING = {
    "checking_account": {
        1: "Sem conta corrente",
        2: "Saldo inferior a 0 DM",
        3: "Saldo entre 0 e 200 DM",
        4: "Saldo acima de 200 DM ou salário",
    },
    "credit_history": {
        0: "Atrasos anteriores",
        1: "Conta crítica ou créditos em outras instituições",
        2: "Sem créditos ou todos pagos corretamente",
        3: "Créditos existentes pagos corretamente até o momento",
        4: "Todos os créditos neste banco pagos corretamente",
    },
    "purpose": {
        0: "Outros",
        1: "Automóvel novo",
        2: "Automóvel usado",
        3: "Móveis ou equipamentos",
        4: "Rádio ou televisão",
        5: "Eletrodomésticos",
        6: "Reparos",
        7: "Educação",
        8: "Férias",
        9: "Requalificação profissional",
        10: "Negócio",
    },
    "savings_account": {
        1: "Desconhecida ou sem poupança",
        2: "Menos de 100 DM",
        3: "Entre 100 e 500 DM",
        4: "Entre 500 e 1.000 DM",
        5: "Acima de 1.000 DM",
    },
    "employment_duration": {
        1: "Desempregado",
        2: "Menos de 1 ano",
        3: "Entre 1 e 4 anos",
        4: "Entre 4 e 7 anos",
        5: "7 anos ou mais",
    },
    "installment_rate": {
        1: "35% ou mais",
        2: "Entre 25% e 35%",
        3: "Entre 20% e 25%",
        4: "Menos de 20%",
    },
    "personal_status_sex": {
        1: "Homem divorciado ou separado",
        2: "Mulher não solteira ou homem solteiro",
        3: "Homem casado ou viúvo",
        4: "Mulher solteira",
    },
    "guarantors": {
        1: "Nenhum",
        2: "Coobrigado",
        3: "Fiador",
    },
    "residence_duration": {
        1: "Menos de 1 ano",
        2: "Entre 1 e 4 anos",
        3: "Entre 4 e 7 anos",
        4: "7 anos ou mais",
    },
    "property": {
        1: "Desconhecido ou sem propriedade",
        2: "Automóvel ou outro bem",
        3: "Poupança habitacional ou seguro de vida",
        4: "Imóvel",
    },
    "other_installment_plans": {
        1: "Banco",
        2: "Lojas",
        3: "Nenhum",
    },
    "housing": {
        1: "Moradia gratuita",
        2: "Alugada",
        3: "Própria",
    },
    "existing_credits": {
        1: "1 crédito",
        2: "Entre 2 e 3 créditos",
        3: "Entre 4 e 5 créditos",
        4: "6 créditos ou mais",
    },
    "job": {
        1: "Desempregado ou não qualificado não residente",
        2: "Não qualificado residente",
        3: "Qualificado ou funcionário",
        4: "Gestor, autônomo ou profissional altamente qualificado",
    },
    "people_liable": {
        1: "3 ou mais pessoas",
        2: "Até 2 pessoas",
    },
    "telef": {
        1: "Não",
        2: "Sim",
    },
    "foreign_worker": {
        1: "Sim",
        2: "Não",
    },
    "credit_risk": {
        0: "Mau risco",
        1: "Bom risco",
    },
}
