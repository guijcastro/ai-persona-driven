"""
Processador de Prompts para Persona Professional AI Builder
Módulo completo para gerenciamento do fluxo de 10 etapas
"""

import os
import yaml
from typing import Dict, List, Optional

class PromptProcessor:
    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = prompts_dir
        self.steps = {
            1: "ponto-partida",
            2: "material-base", 
            3: "entrevista-guiada",
            4: "diagnostico-linguagem",
            5: "revisao-emocional",
            6: "analise-canais",
            7: "critica-brutal",
            8: "persona-narrativa",
            9: "percepcao-externa",
            10: "ajustes-finais"
        }
        
        # Carregar configurações
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Carrega configurações do arquivo YAML"""
        try:
            with open("config.yaml", "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return {
                "process": {"steps": 10, "sequential": True},
                "output": {"persona_length": "500-800 palavras"}
            }
    
    def load_prompt(self, step_number: int) -> str:
        """Carrega o prompt da etapa especificada"""
        if step_number not in self.steps:
            raise ValueError(f"Etapa {step_number} não existe")
        
        filename = f"etapa-{step_number}-{self.steps[step_number]}.md"
        filepath = os.path.join(self.prompts_dir, filename)
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                return self.validate_prompt_structure(content, step_number)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo do prompt não encontrado: {filename}")
    
    def validate_prompt_structure(self, content: str, step_number: int) -> str:
        """Valida a estrutura básica do prompt"""
        required_sections = ["Objetivo", "Regras", "Entradas", "Entregáveis", "Encerramento obrigatório"]
        
        for section in required_sections:
            if section not in content:
                print(f"⚠️  Aviso: Seção '{section}' não encontrada no prompt da etapa {step_number}")
        
        return content
    
    def get_step_requirements(self, step_number: int) -> List[str]:
        """Retorna requisitos específicos de cada etapa"""
        requirements = {
            1: ["situacao_atual", "direcao_desejada", "motivacao", "aprendizados", "medos", "sonhos"],
            2: ["curriculo", "bio_linkedin", "textos_representativos", "sintese_pessoal"],
            3: ["entrevista_motivacao", "entrevista_estilo", "entrevista_impacto", "entrevista_relacoes", "entrevista_fronteiras", "entrevista_evolucao"],
            4: ["padroes_linguagem", "valores_explicitos_implicitos", "proposta_valor", "tensoes", "tom_predominante", "pontos_densidade_ruido", "alavancas_clareza"],
            5: ["matriz_emocao_evidencia_risco_ajuste", "objetivos_emocionais", "decisoes_editoriais", "habitos_evitar"],
            6: ["quadro_canais", "expressoes_preferidas_proibidas", "microexemplos_canais"],
            7: ["critica_generico_posado", "falta_evidencia", "jargoes_cortar", "reescrita_frases", "principios_editoriais"],
            8: ["persona_essencia", "persona_papel", "persona_modo_operacao", "persona_impacto", "persona_fronteiras", "persona_linha_tempo", "teste_autenticidade"],
            9: ["perfil_recrutador", "perfil_linkedin", "perfil_psicologo", "perfil_comercial", "perfil_tecnico", "sintese_convergencias"],
            10: ["persona_final", "nota_tecnica_ajustes", "checklist_coerencia_final"]
        }
        return requirements.get(step_number, [])
    
    def validate_step_completion(self, step_number: int, user_responses: Dict) -> bool:
        """Valida se todas as respostas necessárias foram fornecidas"""
        required = self.get_step_requirements(step_number)
        return all(req in user_responses for req in required)
    
    def generate_step_summary(self, step_number: int, responses: Dict) -> str:
        """Gera um resumo da etapa completada"""
        summary_templates = {
            1: "📌 **Etapa 1 - Ponto de Partida Concluída**\n- Situação atual definida\n- Direção desejada estabelecida\n- Motivações e desafios mapeados",
            2: "📁 **Etapa 2 - Base de Dados Consolidada**\n- Material factual reunido\n- Padrões de linguagem identificados\n- Valores emergentes catalogados",
            # ... templates para todas as etapas
        }
        return summary_templates.get(step_number, f"✅ Etapa {step_number} concluída")
    
    def get_next_step_instruction(self, current_step: int) -> str:
        """Retorna a instrução para a próxima etapa"""
        if current_step < 10:
            return f"✅ Etapa {current_step} concluída. Copie e cole agora o prompt da Etapa {current_step + 1}."
        else:
            return "✅ Etapa 10 concluída. Trabalho finalizado. Persona consolidada."
    
    def export_persona(self, persona_data: Dict, format: str = "markdown") -> str:
        """Exporta a persona final no formato especificado"""
        if format == "markdown":
            return self._export_markdown(persona_data)
        elif format == "text":
            return self._export_text(persona_data)
        else:
            raise ValueError(f"Formato não suportado: {format}")
    
    def _export_markdown(self, persona_data: Dict) -> str:
        """Exporta em formato Markdown"""
        markdown = f"# Persona Professional - {persona_data.get('nome', 'Usuário')}\n\n"
        
        for section, content in persona_data.items():
            if section != 'nome':
                markdown += f"## {section.replace('_', ' ').title()}\n\n{content}\n\n"
        
        return markdown

# Exemplo de uso
if __name__ == "__main__":
    processor = PromptProcessor()
    
    # Carregar prompt da etapa 1
    try:
        prompt_etapa_1 = processor.load_prompt(1)
        print("Prompt da Etapa 1 carregado com sucesso!")
        print(prompt_etapa_1[:200] + "...")  # Primeiros 200 caracteres
    except Exception as e:
        print(f"Erro ao carregar prompt: {e}")
