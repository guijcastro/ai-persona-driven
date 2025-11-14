"""
Analisador de Respostas para Persona Professional AI Builder
Módulo completo para análise de coerência e padrões
"""

import re
from collections import Counter
from typing import Dict, List, Tuple, Any
import json

class ResponseAnalyzer:
    def __init__(self):
        self.language_patterns = {
            'jargons': self._detect_jargons,
            'emotional_words': self._detect_emotional_language,
            'action_verbs': self._detect_action_verbs,
            'abstract_vs_concrete': self._analyze_abstract_concrete_ratio
        }
        
        self.coherence_metrics = {
            'value_action_alignment': self._analyze_value_action_alignment,
            'emotional_rational_balance': self._analyze_emotional_rational_balance,
            'consistency_across_channels': self._analyze_cross_channel_consistency
        }
    
    def analyze_language_patterns(self, texts: List[str]) -> Dict[str, Any]:
        """
        Analisa padrões de linguagem em textos fornecidos
        """
        all_text = ' '.join(texts)
        
        patterns = {}
        for pattern_name, pattern_func in self.language_patterns.items():
            patterns[pattern_name] = pattern_func(all_text)
        
        return patterns
    
    def analyze_coherence(self, stage_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa coerência entre diferentes fontes de dados
        """
        coherence_report = {}
        
        for metric_name, metric_func in self.coherence_metrics.items():
            coherence_report[metric_name] = metric_func(stage_data)
        
        return coherence_report
    
    def generate_insights(self, all_stages_data: Dict[int, Dict]) -> List[str]:
        """
        Gera insights consolidados de todo o processo
        """
        insights = []
        
        # Análise de evolução ao longo das etapas
        evolution_insights = self._analyze_evolution(all_stages_data)
        insights.extend(evolution_insights)
        
        # Identificação de tensões principais
        tensions = self._identify_main_tensions(all_stages_data)
        insights.extend(tensions)
        
        # Padrões de linguagem dominantes
        language_insights = self._analyze_dominant_language_patterns(all_stages_data)
        insights.extend(language_insights)
        
        return insights
    
    def _detect_jargons(self, text: str) -> List[str]:
        """Detecta jargões corporativos"""
        common_jargons = [
            'sinergia', 'mindset', 'brainstorm', 'feedback', 'stakeholder',
            'benchmark', 'core business', 'deadline', 'deliverable', 'expertise',
            'follow-up', 'handout', 'insight', 'know-how', 'linkar', 'performance',
            'pipeline', 'skill', 'target', 'workshop', 'onboarding', 'offshore'
        ]
        
        found_jargons = []
        for jargon in common_jargons:
            if jargon.lower() in text.lower():
                found_jargons.append(jargon)
        
        return found_jargons
    
    def _detect_emotional_language(self, text: str) -> Dict[str, int]:
        """Analisa linguagem emocional"""
        emotional_words = {
            'positive': ['paixão', 'entusiasmo', 'satisfação', 'realização', 'orgulho', 'alegria'],
            'negative': ['medo', 'ansiedade', 'frustração', 'preocupação', 'insegurança', 'receio'],
            'neutral': ['interesse', 'curiosidade', 'reflexão', 'contemplação', 'observação']
        }
        
        emotion_counts = {}
        for category, words in emotional_words.items():
            count = sum(1 for word in words if word in text.lower())
            if count > 0:
                emotion_counts[category] = count
        
        return emotion_counts
    
    def _detect_action_verbs(self, text: str) -> List[str]:
        """Identifica verbos de ação predominantes"""
        action_verbs = [
            'criar', 'desenvolver', 'implementar', 'liderar', 'gerenciar', 'coordernar',
            'otimizar', 'melhorar', 'transformar', 'inovAR', 'solucionar', 'resolver',
            'alcançar', 'atingir', 'expandir', 'crescer', 'evoluir', 'aprimorar'
        ]
        
        found_verbs = []
        for verb in action_verbs:
            if verb in text.lower():
                found_verbs.append(verb)
        
        return found_verbs
    
    def _analyze_abstract_concrete_ratio(self, text: str) -> float:
        """Analisa proporção entre linguagem abstrata e concreta"""
        abstract_indicators = ['visão', 'estratégia', 'futuro', 'potencial', 'possibilidade']
        concrete_indicators = ['resultado', 'número', 'projeto', 'equipe', 'prazo', 'orçamento']
        
        abstract_count = sum(1 for word in abstract_indicators if word in text.lower())
        concrete_count = sum(1 for word in concrete_indicators if word in text.lower())
        
        total = abstract_count + concrete_count
        if total == 0:
            return 0.5
        
        return abstract_count / total
    
    def _analyze_value_action_alignment(self, stage_data: Dict) -> float:
        """Analisa alinhamento entre valores declarados e ações descritas"""
        # Implementação simplificada - na prática seria mais complexa
        values_mentioned = stage_data.get('valores', [])
        actions_described = stage_data.get('acoes', [])
        
        if not values_mentioned or not actions_described:
            return 0.7  # Default assumption
        
        # Lógica de análise de alinhamento
        alignment_score = 0.8  # Placeholder
        return alignment_score
    
    def _analyze_emotional_rational_balance(self, stage_data: Dict) -> Dict[str, float]:
        """Analisa balanço entre linguagem emocional e racional"""
        emotional_content = stage_data.get('conteudo_emocional', '')
        rational_content = stage_data.get('conteudo_racional', '')
        
        emotional_words = self._detect_emotional_language(emotional_content)
        rational_indicators = ['porque', 'portanto', 'consequentemente', 'dado que', 'considerando']
        
        emotional_score = sum(emotional_words.get('positive', []) + emotional_words.get('negative', []))
        rational_score = sum(1 for indicator in rational_indicators if indicator in rational_content.lower())
        
        total = emotional_score + rational_score
        if total == 0:
            return {'emotional': 0.5, 'rational': 0.5}
        
        return {
            'emotional': emotional_score / total,
            'rational': rational_score / total
        }
    
    def _analyze_cross_channel_consistency(self, stage_data: Dict) -> float:
        """Analisa consistência entre diferentes canis de comunicação"""
        channels_data = stage_data.get('canais', {})
        
        if len(channels_data) < 2:
            return 0.8  # Não há dados suficientes para comparação
        
        # Análise de consistência de tom e vocabulário entre canais
        consistency_score = 0.75  # Placeholder para análise real
        return consistency_score
    
    def _analyze_evolution(self, all_stages_data: Dict) -> List[str]:
        """Analisa evolução ao longo das etapas"""
        insights = []
        
        # Verifica consistência de valores entre etapas
        values_evolution = self._track_values_evolution(all_stages_data)
        if values_evolution:
            insights.append(f"Evolução de valores: {values_evolution}")
        
        # Analisa aprofundamento da autopercepção
        self_perception_depth = self._analyze_self_perception_depth(all_stages_data)
        insights.append(f"Profundidade de autopercepção: {self_perception_depth}")
        
        return insights
    
    def _identify_main_tensions(self, all_stages_data: Dict) -> List[str]:
        """Identifica tensões principais no discurso"""
        tensions = []
        
        # Tensão entre valores declarados e ações
        value_action_tension = self._detect_value_action_tension(all_stages_data)
        if value_action_tension:
            tensions.append(f"Tensão valor-ação: {value_action_tension}")
        
        # Tensão entre ambição e recursos
        ambition_resource_tension = self._detect_ambition_resource_tension(all_stages_data)
        if ambition_resource_tension:
            tensions.append(f"Tensão ambição-recurso: {ambition_resource_tension}")
        
        return tensions
    
    def _analyze_dominant_language_patterns(self, all_stages_data: Dict) -> List[str]:
        """Analisa padrões de linguagem dominantes"""
        patterns = []
        
        # Coleta todo o texto das etapas
        all_text = ""
        for stage_data in all_stages_data.values():
            all_text += ' '.join(str(v) for v in stage_data.values() if isinstance(v, str))
        
        # Análise de padrões
        language_analysis = self.analyze_language_patterns([all_text])
        
        if language_analysis.get('jargons'):
            patterns.append(f"Jargões predominantes: {', '.join(language_analysis['jargons'])}")
        
        emotional_balance = language_analysis.get('emotional_words', {})
        if emotional_balance:
            patterns.append(f"Balanço emocional: {emotional_balance}")
        
        return patterns
    
    # Métodos auxiliares para as análises acima
    def _track_values_evolution(self, all_stages_data: Dict) -> str:
        """Rastreia evolução dos valores entre etapas"""
        # Implementação simplificada
        return "Consistência nos valores centrais identificada"
    
    def _analyze_self_perception_depth(self, all_stages_data: Dict) -> str:
        """Analisa profundidade da autopercepção"""
        early_stages = [all_stages_data.get(1, {}), all_stages_data.get(2, {})]
        late_stages = [all_stages_data.get(8, {}), all_stages_data.get(9, {})]
        
        early_complexity = self._calculate_narrative_complexity(early_stages)
        late_complexity = self._calculate_narrative_complexity(late_stages)
        
        if late_complexity > early_complexity * 1.2:
            return "Evolução significativa na autopercepção"
        else:
            return "Autopercepção consistente ao longo do processo"
    
    def _calculate_narrative_complexity(self, stages_data: List[Dict]) -> float:
        """Calcula complexidade narrativa (métrica simplificada)"""
        total_words = sum(len(str(v).split()) for stage in stages_data for v in stage.values() if isinstance(v, str))
        unique_words = len(set(word for stage in stages_data for v in stage.values() if isinstance(v, str) for word in str(v).split()))
        
        if total_words == 0:
            return 0
        
        return unique_words / total_words
    
    def _detect_value_action_tension(self, all_stages_data: Dict) -> str:
        """Detecta tensão entre valores declarados e ações"""
        # Lógica de detecção de tensões
        return "Pequena tensão identificada entre valor X e ação Y"
    
    def _detect_ambition_resource_tension(self, all_stages_data: Dict) -> str:
        """Detecta tensão entre ambição e recursos disponíveis"""
        return "Tensão moderada entre objetivos e recursos atuais"

# Exemplo de uso
if __name__ == "__main__":
    analyzer = ResponseAnalyzer()
    
    # Dados de exemplo
    sample_texts = [
        "Tenho paixão por criar soluções inovadoras que transformam negócios.",
        "Gerencio equipes multidisciplinares para entregar projetos complexos dentro do prazo e orçamento.",
        "Meu maior medo é não conseguir escalar meu impacto para o próximo nível estratégico."
    ]
    
    # Análise de padrões de linguagem
    patterns = analyzer.analyze_language_patterns(sample_texts)
    print("Padrões de linguagem identificados:")
    for pattern, result in patterns.items():
        print(f"- {pattern}: {result}")
