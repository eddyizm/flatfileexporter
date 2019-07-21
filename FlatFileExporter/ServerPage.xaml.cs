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
            PopulateServerList();
        }

        private void PopulateServerList()
        {
            lv_server.Items.Clear();
            var sCount = Properties.Settings.Default.Servers.Count;
            if (sCount > 0)
            {
                string[] serverList = new string[sCount];
                Properties.Settings.Default.Servers.CopyTo(serverList, 0);
                foreach (var x in serverList)
                {
                    lv_server.Items.Add(x);
                }
            }
        }

                
        private void AddServer(string server)
        {
            try
            {
                // TODO Check if setting exists
                Properties.Settings.Default.Servers.Add(server);
                Properties.Settings.Default.Save();
                ServerTextBox.Text = "";
                PopulateServerList();
            }
            catch (NullReferenceException ex )
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void btnDelete_Click(object sender, RoutedEventArgs e)
        {

            try
            {
                if (lv_server.SelectedValue != null)
                {
                    var delServer = lv_server.SelectedValue.ToString();
                    var result = MessageBox.Show($"Remove \"{delServer}\"?", "Remove Server", MessageBoxButton.OKCancel);
                    if (result == MessageBoxResult.OK)
                    {
                        RemoveServer(delServer);
                    }
                }
                else
                { MessageBox.Show($"Please select an item to delete"); }
            }
            catch (Exception ex)
            {

                MessageBox.Show($"Oops, please close application and try again. Error:{ex.ToString()}");
            }
            
            
        }

        private void RemoveServer(string server)
        {
            try
            {
                // TODO Check if setting exists
                Properties.Settings.Default.Servers.Remove(server);
                Properties.Settings.Default.Save();
                ServerTextBox.Text = "";
                PopulateServerList();
            }
            catch (NullReferenceException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void btnAddServer_Click(object sender, RoutedEventArgs e)
        {
            var nServer = ServerTextBox.Text;
            if (string.IsNullOrEmpty(nServer))
            {
                MessageBox.Show("Please enter a valid server");
                return;
            }
            var result = MessageBox.Show($"Add Server \"{nServer}\" to list?", "Add Server", MessageBoxButton.OKCancel);
            if (result == MessageBoxResult.OK)
            {
                AddServer(nServer);
                
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
            {
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new MainPage();
            }
                
        }
    }
}
