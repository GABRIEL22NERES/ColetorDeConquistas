class WidgetStore:
    def __init__(self):
        self._widgets = {}

    def add_widget(self, section, widget_name, widget):
        """
        Adiciona um widget ao armazenamento
        
        Args:
            section (str): Seção do widget (ex: 'header', 'body', 'footer')
            widget_name (str): Nome identificador do widget
            widget: O widget a ser armazenado
        """
        if section not in self._widgets:
            self._widgets[section] = {}
            
        self._widgets[section][widget_name] = widget

    def get_widget(self, section, widget_name):
        """
        Recupera um widget específico
        
        Args:
            section (str): Seção do widget
            widget_name (str): Nome do widget
            
        Returns:
            O widget solicitado ou None se não encontrado
        """
        return self._widgets.get(section, {}).get(widget_name)
    
    def get_section(self, section):
        """
        Recupera todos os widgets de uma seção
        
        Args:
            section (str): Nome da seção
            
        Returns:
            dict: Dicionário com todos os widgets da seção
        """
        return self._widgets.get(section, {})
    
    def remove_widget(self, section, widget_name):
        """
        Remove um widget do armazenamento
        
        Args:
            section (str): Seção do widget
            widget_name (str): Nome do widget
        """
        if section in self._widgets and widget_name in self._widgets[section]:
            del self._widgets[section][widget_name]


    def add_tasks_list(self, section, tasks_dict):
        """
        Adiciona uma lista de tarefas completa ao armazenamento

        Args:
            section (str): Seção para armazenar (ex: 'task_list')
            tasks_dict (dict): Dicionário já estruturado com as tarefas
                Exemplo do formato:
                {
                    "row1": {
                        "div_column_row": widget1,
                        "text_value_column": widget2
                    },
                    "row2": {
                        "div_column_row": widget3,
                        "text_value_column": widget4
                    }
                }
        """
        if section not in self._widgets:
            self._widgets[section] = {}

        self._widgets[section].update(tasks_dict)
