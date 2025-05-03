#!/usr/bin/env python
# coding: utf-8
import re
from typing import Dict, Any, List, Optional

class LessonExplainer:
    """
    Generates explanations for educational content in a conversational, teacher-like style.
    """

    def __init__(self):
        """Initialize the lesson explainer."""
        # Placeholder for future model integration or configuration
        # Define a maximum character limit to avoid overly long explanations for very large documents
        self.MAX_TEXT_CHARS_FOR_EXPLANATION = 10000 # Approx 1500-2000 words
        pass

    def generate_explanation(self, text: str, complexity_level: str = "medium", source_filename: Optional[str] = None) -> str:
        """
        Generate a conversational, teacher-like explanation for the given text.
        Considers the full text up to a reasonable limit.

        Args:
            text: The text content to explain.
            complexity_level: Desired complexity level (simple, medium, advanced).
            source_filename: The name of the source file (optional, for context).

        Returns:
            Conversational explanation of the content.
        """
        # Remove excessive whitespace and normalize text
        processed_text = self._preprocess_text(text)

        if not processed_text.strip():
            return "I don't see any content to explain. Please upload some material first."

        # Limit text length to prevent excessive processing time / cost
        if len(processed_text) > self.MAX_TEXT_CHARS_FOR_EXPLANATION:
            processed_text = processed_text[:self.MAX_TEXT_CHARS_FOR_EXPLANATION]
            warning = "(Note: The explanation is based on the first part of the document due to its length.)\n\n"
        else:
            warning = ""

        # Identify the subject matter
        subject = self._identify_subject(processed_text, source_filename)

        # Generate explanation based on complexity level
        # For now, we focus on enhancing the medium level significantly
        if complexity_level == "simple":
            explanation = self._generate_simple_explanation(processed_text, subject)
        elif complexity_level == "advanced":
            explanation = self._generate_advanced_explanation(processed_text, subject)
        else:  # medium (default)
            explanation = self._generate_teacher_explanation(processed_text, subject)

        return warning + explanation

    def _preprocess_text(self, text: str) -> str:
        """
        Preprocess text by removing excessive whitespace and normalizing.

        Args:
            text: Raw text to preprocess.

        Returns:
            Preprocessed text.
        """
        # Replace multiple newlines with a single newline
        text = re.sub(r'\n{3,}', '\n\n', text)
        # Replace multiple spaces with a single space
        text = re.sub(r' {2,}', ' ', text)
        # Attempt to fix common OCR issues like ligatures or misinterpretations
        text = text.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
        # Remove page numbers or headers/footers if possible (simple example)
        text = re.sub(r'^\s*Page \d+\s*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*Chapter \d+\s*$', '', text, flags=re.MULTILINE)

        return text.strip()

    def _identify_subject(self, text: str, source_filename: Optional[str] = None) -> str:
        """
        Attempt to identify the subject matter of the text, using filename as a hint.

        Args:
            text: The text content to analyze.
            source_filename: The name of the source file (optional).

        Returns:
            Identified subject or "general" if unclear.
        """
        text_lower = text.lower()
        filename_lower = source_filename.lower() if source_filename else ""

        # Prioritize filename hints
        if "ratio" in filename_lower or "math" in filename_lower or "algebra" in filename_lower or "geometry" in filename_lower:
            return "mathematics"
        if "history" in filename_lower:
            return "history"
        if "science" in filename_lower or "biology" in filename_lower or "chemistry" in filename_lower or "physics" in filename_lower:
            return "science"
        if "literature" in filename_lower or "novel" in filename_lower or "poem" in filename_lower:
            return "literature"
        if "language" in filename_lower or "grammar" in filename_lower or "vocabulary" in filename_lower:
            return "language"

        # Fallback to text content analysis
        if any(term in text_lower for term in ['ratio', 'equation', 'formula', 'calculation', 'algebra', 'geometry', 'solve for x', 'fraction', 'decimal', 'percent']):
            return "mathematics"
        if any(term in text_lower for term in ['history', 'century', 'war', 'civilization', 'ancient', 'revolution', 'president', 'king', 'queen']):
            return "history"
        if any(term in text_lower for term in ['science', 'biology', 'chemistry', 'physics', 'experiment', 'molecule', 'atom', 'cell', 'energy', 'force']):
            return "science"
        if any(term in text_lower for term in ['literature', 'novel', 'poem', 'author', 'character', 'story', 'theme', 'metaphor', 'symbolism']):
            return "literature"
        if any(term in text_lower for term in ['grammar', 'vocabulary', 'language', 'verb', 'noun', 'adjective', 'sentence', 'paragraph']):
            return "language"

        return "general"

    def _generate_teacher_explanation(self, text: str, subject: str) -> str:
        """
        Generate a detailed, teacher-like explanation with examples based on the full text (up to limit).

        Args:
            text: The text content to explain.
            subject: Identified subject matter.

        Returns:
            Teacher-like explanation.
        """
        # --- This is still a placeholder for a more sophisticated LLM call --- #
        # The logic below simulates a slightly better explanation based on more text
        # but a real LLM would provide much better quality and coherence.

        intro = f"Alright, let's dive into this material on {subject}! I'll break it down for you step-by-step, just like we would in class. Don't worry if it seems tricky at first, we'll figure it out together.\n\n"
        body = "Based on the text provided, here are the main points I see:\n\n"
        examples = ""
        summary = ""
        outro = "\n\nSo, that's a walkthrough of the key ideas in the material provided! How does that sound? Remember, practice makes perfect. If any part is still unclear, please ask! I'm here to help you understand."

        # Simulate extracting key points/paragraphs from the *entire* text (up to the limit)
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        num_paragraphs_to_summarize = min(len(paragraphs), 5) # Summarize up to 5 paragraphs

        for i in range(num_paragraphs_to_summarize):
            para = paragraphs[i]
            # Simple summary of the paragraph
            body += f"**Paragraph {i+1}:** This part discusses '{para[:80]}...'. It seems to be explaining [your interpretation/summary of the paragraph's main idea].\n"

        # Add subject-specific examples/summary if possible
        if subject == "mathematics":
            if "ratio" in text.lower():
                examples = ("\n\n**Let's look at an example related to ratios:** Imagine you have a fruit bowl with 5 apples and 10 oranges. \n" 
                            "- The ratio of apples to oranges is 5 to 10, or 5:10, or 5/10. \n" 
                            "- We can simplify this! Both 5 and 10 are divisible by 5. So, the simplified ratio is 1:2. This means for every 1 apple, there are 2 oranges.\n" 
                            "- What about the ratio of oranges to *total* fruit? There are 10 oranges and 15 total fruits (5 apples + 10 oranges). So the ratio is 10:15. Can we simplify this? Yes! Both are divisible by 5, giving us 2:3. For every 3 pieces of fruit, 2 are oranges.")
                summary = "\n\n**Key Takeaways on Ratios:**\n1. A ratio compares two quantities.\n2. You can write ratios using 'to', a colon (:), or as a fraction.\n3. The order matters! Make sure you match the order asked in the question.\n4. Ratios can often be simplified like fractions by dividing both parts by a common factor."
            else:
                examples = "\n\nFor instance, if we're solving an equation like 2x + 3 = 11, the goal is to find the value of 'x'. We'd typically isolate 'x' by performing inverse operations..."
                summary = "\n\nRemember the key steps for this type of math problem: [Summarize steps/concepts]."

        elif subject == "history":
            examples = "\n\nThink about it like this: If we're studying the American Revolution, we'd look at the causes (like taxes), the key people (like George Washington), and the results (like the creation of the USA)..."
            summary = "\n\nMain points to remember about this historical period are: [Summarize key events/causes/effects]."

        elif subject == "science":
            examples = "\n\nFor example, if we're learning about photosynthesis, plants use sunlight, water, and carbon dioxide to make their own food (sugar) and release oxygen. It's like they're tiny food factories!"
            summary = "\n\nKey scientific ideas here are: [Summarize concepts/processes]."

        else: # General subject
            examples = "\n\nWe can relate this to everyday life. For example..."
            summary = "\n\nIn short, the text explains: [Summarize]."

        # Combine parts
        explanation = intro + body + examples + summary + outro
        return explanation

    # Keep the simple and advanced placeholders, but focus was on medium/teacher
    def _generate_simple_explanation(self, text: str, subject: str) -> str:
        """
        Generate a simple explanation suitable for younger students.
        (Placeholder - less detailed than teacher explanation)
        """
        # Process a smaller portion for simple explanation
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        first_para = paragraphs[0] if paragraphs else ""
        explanation = f"Hi there! Let's look at this {subject} topic. It's basically saying that... '{first_para[:100]}...'. For example, think about... [Simple analogy]. Does that help a bit?"
        return explanation

    def _generate_advanced_explanation(self, text: str, subject: str) -> str:
        """
        Generate an advanced explanation for older or advanced students.
        (Placeholder - more formal than teacher explanation)
        """
        # Process more text for advanced explanation
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        key_concepts = []
        for i in range(min(len(paragraphs), 3)):
             key_concepts.append(f"[Inferred Key Concept {i+1} from paragraph {i+1}]" )

        explanation = f"Analyzing this text on {subject}, we can discern several key principles. Firstly, the concept of {key_concepts[0]} is introduced... This relates to {key_concepts[1]}... Furthermore, {key_concepts[2]}... A critical perspective might consider... In essence, the material argues that... Would you like a deeper dive into any specific aspect?"
        return explanation
