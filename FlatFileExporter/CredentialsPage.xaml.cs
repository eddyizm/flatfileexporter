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
    /// Interaction logic for Credentials.xaml
    /// </summary>
    public partial class CredentialsPage : Page
    {
        public CredentialsPage()
        {
            InitializeComponent();
            LoadCredentials();
        }

        private void LoadCredentials()
        {
            try
            {
                if (!string.IsNullOrEmpty(Properties.Settings.Default.Username))
                {
                    txUserName.Text = Properties.Settings.Default.Username;
                }
            }
            catch (Exception ex)
            {
                throw;
            }
            
        }

        private void ExUserPass_Expanded(object sender, RoutedEventArgs e)
        {
            exTrustConnnect.IsExpanded = false;
        }

        private void btnClear_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
            {
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new MainPage();
            }
        }

        private void btnSaveCred_Click(object sender, RoutedEventArgs e)
        {

            try
            {
                Properties.Settings.Default.Username = txUserName.Text;
                //Properties.Settings.Default.Password = txPassword.Text;
                Properties.Settings.Default.Save();
                
            }
            catch (NullReferenceException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }
    }
}
