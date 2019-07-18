using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for ServerPage.xaml
    /// </summary>
    public partial class ServerPage : Page
    {
        public ServerPage()
        {
            InitializeComponent();
        }

        private void btnAddServer_Click(object sender, RoutedEventArgs e)
        {
            var nServer = ServerTextBox.Text;
            MessageBox.Show($"Add Server - {nServer}");

        }

        private void btnDelete_Click(object sender, RoutedEventArgs e)
        {
            if (lv_server.SelectedValue != null)
            {
                var nipples = ((ListBoxItem)lv_server.SelectedValue).Content.ToString();
                MessageBox.Show($"{nipples}: To Delete");
            }
            else
            { MessageBox.Show($"Please select an item to delete"); }
           
            
        }
    }
}
