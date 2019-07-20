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
            // MessageBox.Show($"Add Server - {nServer}");
            IsValid(nServer);
            AddSettings(nServer);

        }

        private bool IsValid(string nServer)
        {

            return (nServer.Length > 1 ? true : false);
        }

        private void AddSettings(string server)
        {

            try
            {
                // TODO Check if setting exists
                // TODO Confirm before saving 
                Properties.Settings.Default.Servers.Add(server);
                Properties.Settings.Default.Save();
            }
            catch (NullReferenceException ex )
            {
                MessageBox.Show(ex.ToString());
            }
            
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
