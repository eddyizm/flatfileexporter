
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Resources;
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


namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            _mainFrame.Navigate(new MainPage());
            //PopulateServerItems();

            //// TODO // may need to pull this from python cli instead or figure out a way to keep them in sync. 
            //// Check version. 
            //var ver = typeof(MainWindow).Assembly.GetName().Version.ToString();
            //MessageBox.Show(ver);
            ///

            //MessageBox.Show("--------------------DEBUGGING-------------------------------");
            //MessageBox.Show(Properties.Settings.Default.IsFirstRun.ToString());
            //SettingsDebugMethod();
            //LoadServers();
            LoadDataBaseList();
            
        }

        private void LoadDataBaseList()
        {
            var dbCount = Properties.Settings.Default.Databases.Count;
            if (dbCount > 0)
            {
                string[] dbList = new string[dbCount];
                Properties.Settings.Default.Databases.CopyTo(dbList, 0);
                foreach (var x in dbList)
                {
                    if (x.Length > 0)
                        MessageBox.Show($"{x}");
                }
                    
                
            }
        }

        private void LoadServers()
        {
            var sCount = Properties.Settings.Default.Servers.Count;
            if (sCount > 0)
            {
                string[] serverList = new string[sCount];
                Properties.Settings.Default.Servers.CopyTo(serverList, 0);
                foreach (var x in serverList)
                {
                    if (x.Length > 0)
                        MessageBox.Show($"{x}");
                }
            }
            
        }

        private static void SettingsDebugMethod()
        {
            // check settings 
            Console.WriteLine("--------------------DEBUGGING-------------------------------");
            MessageBox.Show("--------------------DEBUGGING-------------------------------");
            MessageBox.Show(Properties.Settings.Default.IsFirstRun.ToString());
            Console.WriteLine(Properties.Settings.Default.IsFirstRun.ToString());

            if (Properties.Settings.Default.IsFirstRun == true)
            {
                Properties.Settings.Default.IsFirstRun = false;
                MessageBox.Show("Moving into if statement and changing to false");
                Properties.Settings.Default.Save();
            }
            Console.WriteLine("--------------------DEBUGGING-------------------------------");

            // will need this code to maintain future settings when upgraded
            //Properties.Settings.Default.Upgrade();
            //Properties.Settings.Default.Reset();
            //Properties.Settings.Default.Reload();
        }

        private void Menu_Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

              

        private void PopupBox_Closed(object sender, RoutedEventArgs e)
        {

        }

        //private void Menu_Server_Click(object sender, RoutedEventArgs e)
        //{
        //    ServerPage toolsServer = new ServerPage();
        //    this.Content = toolsServer;
        //}

        private void BtnAddServer_Click(object sender, RoutedEventArgs e)
        {

        }

      
        //// combo box populate
        //public ObservableCollection<ComboBoxItem> CbServerItems { get; set; }
        //public ComboBoxItem SelectedcbServerItem { get; set; }
        
        //private void PopulateServerItems()
        //{
        //    // TODO pull from user settings.
        //    DataContext = this;
        //    CbServerItems = new ObservableCollection<ComboBoxItem>();
        //    var cbServerItem = new ComboBoxItem { Content = "<--Select-->" };
        //    SelectedcbServerItem = cbServerItem;
        //    CbServerItems.Add(cbServerItem);
        //    CbServerItems.Add(new ComboBoxItem { Content = "Option 1" });
        //    CbServerItems.Add(new ComboBoxItem { Content = "Option 2" });
        //}

        private void MenuItem_Server_Click(object sender, RoutedEventArgs e)
        {
            _mainFrame.Navigate(new ServerPage());
        }
    }
}
