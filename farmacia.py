from datetime import datetime

class FarmaciaBrinquedoSimulada:
    def __init__(self):
        """Versão simulada que não precisa de MongoDB"""
        print("🎉 Modo simulação ativado! (Sem MongoDB necessário)")
        self.remedinhos = []
        self.preparar_caixinha()
    
    def preparar_caixinha(self):
        """Coloca 4 remedinhos especiais na caixa"""
        self.remedinhos = [
            {
                "_id": "1",
                "nome": "Paracetamol",
                "preco": 15.90,
                "quantidade": 50,
                "tipo": "Analgésico",
                "data_criacao": datetime.now()
            },
            {
                "_id": "2", 
                "nome": "Amoxicilina",
                "preco": 29.50,
                "quantidade": 30,
                "tipo": "Antibiótico",
                "data_criacao": datetime.now()
            },
            {
                "_id": "3",
                "nome": "Loratadina",
                "preco": 12.75,
                "quantidade": 40,
                "tipo": "Antialérgico",
                "data_criacao": datetime.now()
            },
            {
                "_id": "4",
                "nome": "Omeprazol",
                "preco": 18.30,
                "quantidade": 45,
                "tipo": "Antiácido",
                "data_criacao": datetime.now()
            }
        ]
        print("✅ Caixinha preparada com 4 remedinhos mágicos!")
    
    def ver_remedinhos(self):
        """Mostra todos os remedinhos da caixa - READ"""
        print("\n🌈 REMEDINHOS NA CAIXINHA (SIMULAÇÃO):")
        print("=" * 50)
        
        for remedinho in self.remedinhos:
            print(f"\n📦 ID: {remedinho['_id']}")
            print(f"   Nome: {remedinho['nome']}")
            print(f"   Preço: R${remedinho['preco']:.2f}")
            print(f"   Quantidade: {remedinho['quantidade']}")
            print(f"   Tipo: {remedinho['tipo']}")
            print(f"   Criado em: {remedinho['data_criacao'].strftime('%d/%m/%Y')}")
            print("-" * 30)
    
    def criar_remedinho(self):
        """Cria um novo remedinho - CREATE"""
        print("\n🎨 Vamos criar um remedinho novo!")
        
        try:
            nome = input("Qual o nome do remedinho? ").strip()
            preco = float(input("Quanto custa? R$ "))
            quantidade = int(input("Quantos temos? "))
            tipo = input("Que tipo é? ").strip()
            
            novo_remedinho = {
                "_id": str(len(self.remedinhos) + 1),
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade,
                "tipo": tipo,
                "data_criacao": datetime.now()
            }
            
            self.remedinhos.append(novo_remedinho)
            print(f"✅ {nome} foi colocado na caixinha! ID: {novo_remedinho['_id']}")
            
        except ValueError:
            print("❌ Oops! Digite números para preço e quantidade!")
        except Exception as e:
            print(f"❌ Não consegui criar o remedinho: {e}")
    
    def atualizar_remedinho(self):
        """Atualiza um remedinho - UPDATE"""
        print("\n✏️ Vamos mudar um remedinho!")
        self.ver_remedinhos()
        
        try:
            id_remedinho = input("\n📝 Qual o ID do remedinho que quer mudar? ").strip()
            
            # Encontra o remedinho
            remedinho = next((r for r in self.remedinhos if r['_id'] == id_remedinho), None)
            
            if not remedinho:
                print("❌ Não encontrei esse remedinho!")
                return
            
            print("\nO que quer mudar?")
            print("1. 📛 Nome")
            print("2. 💰 Preço")
            print("3. 🔢 Quantidade")
            print("4. 🏷️ Tipo")
            print("5. 🎯 Tudo")
            
            opcao = input("Escolha (1-5): ").strip()
            
            if opcao in ["1", "5"]:
                remedinho["nome"] = input("Novo nome: ").strip()
            if opcao in ["2", "5"]:
                remedinho["preco"] = float(input("Novo preço: R$ "))
            if opcao in ["3", "5"]:
                remedinho["quantidade"] = int(input("Nova quantidade: "))
            if opcao in ["4", "5"]:
                remedinho["tipo"] = input("Novo tipo: ").strip()
            
            remedinho["data_atualizacao"] = datetime.now()
            print("✅ Remedinho mudado com sucesso!")
                
        except Exception as e:
            print(f"❌ Oops! Algo deu errado: {e}")
    
    def deletar_remedinho(self):
        """Deleta um remedinho - DELETE"""
        print("\n🗑️ Vamos tirar um remedinho da caixa!")
        self.ver_remedinhos()
        
        try:
            id_remedinho = input("\n❌ Qual o ID do remedinho que quer tirar? ").strip()
            
            # Confirmação
            certeza = input("Tem certeza? (s/n): ").lower().strip()
            if certeza != 's':
                print("✅ Operação cancelada!")
                return
            
            # Remove o remedinho
            self.remedinhos = [r for r in self.remedinhos if r['_id'] != id_remedinho]
            print("✅ Remedinho tirado da caixa!")
                
        except Exception as e:
            print(f"❌ Oops! Algo deu errado: {e}")
    
    def menu_principal(self):
        """Menu principal do nosso brinquedo"""
        print("🧸 Bem-vindo ao Brinquedo Farmácia MongoDB (Modo Simulação)!")
        
        while True:
            print("\n" + "="*50)
            print("🎪 MENU PRINCIPAL")
            print("="*50)
            print("1. 👀 Ver todos os remedinhos")
            print("2. 🎨 Criar remedinho novo")
            print("3. ✏️ Mudar remedinho")
            print("4. 🗑️ Tirar remedinho")
            print("5. 🚪 Sair do brinquedo")
            print("="*50)
            
            escolha = input("O que quer fazer? (1-5): ").strip()
            
            if escolha == "1":
                self.ver_remedinhos()
            elif escolha == "2":
                self.criar_remedinho()
            elif escolha == "3":
                self.atualizar_remedinho()
            elif escolha == "4":
                self.deletar_remedinho()
            elif escolha == "5":
                print("👋 Tchau! Obrigado por brincar!")
                break
            else:
                print("❌ Escolha inválida! Tenta de novo.")

# Vamos começar a brincadeira!
if __name__ == "__main__":
    brinquedo = FarmaciaBrinquedoSimulada()
    brinquedo.menu_principal()